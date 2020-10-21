import cv2
import numpy as np
from matplotlib import pyplot as plt


# function to rotate image by any angle
def image_rotate_angles_2D(image, rotate_degree, center=None):
    # get the shape of the image
    (h, w) = image.shape[:2]

    # the center is the center of the image by default
    if center is None:
        center = (w / 2, h / 2)

    # rotate the image
    M = cv2.getRotationMatrix2D(center, rotate_degree, 1)
    image_rotated = cv2.warpAffine(image, M, (w, h))

    # return
    return image_rotated


# function to calculate the delta image of two images and its std and ave
def delta_calculation(image_ori, image_rot):
    delta_result_float = image_ori.astype(np.int16) - image_rot.astype(np.int16)
    std_delta_result_float = delta_result_float.std()
    ave_delta_result_float = delta_result_float.mean()

    return delta_result_float, std_delta_result_float, ave_delta_result_float


# save(plot) the delta image, original image and rotated image
def plot_image(image_path, theta, verbose=None):
    # load the image file
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # rotate the image by theta following by -theta
    image_rotate_theta = image_rotate_angles_2D(image, theta)
    image_rotate_rev_theta = image_rotate_angles_2D(image_rotate_theta, -1 * theta)

    # calculate the delta, std and ave of the delta
    delta_result_float, std_delta_result_float, ave_delta_result_float = delta_calculation(image,
                                                                                           image_rotate_rev_theta)
    # stack the delta(absolute value), image, image_rotate_rev_theta
    image_hstack = np.hstack((abs(delta_result_float), image, image_rotate_rev_theta))

    # save the stacked image
    cv2.imwrite(image_path.replace('.jpeg', '_theta={}_std={}_ave={}.jpeg'.format(theta, std_delta_result_float,
                                                                                  ave_delta_result_float)),
                image_hstack)

    # show the stacked image
    if verbose == True:
        plt.imshow(image_hstack, 'gray')
        plt.title('{} -- theta={}'.format(image_path.split('/')[-1], theta))
        print('{}, theta is {}, std of the delta image is {}, ave of the delta image is {}'.format(
            image_path.split('/')[-1], theta,
            std_delta_result_float,
            ave_delta_result_float))
        plt.pause(0.5)
        plt.close()

    return std_delta_result_float, ave_delta_result_float


# main function, save(plot) the curves
def plot_curve(theta_list, image_path):
    list_std_delta_result_float = []
    list_ave_delta_result_float = []

    # calculate the std and ave values of the delta images
    for theta in theta_list:
        # if need to show the delta image, original image and rotated image, set the verbose to True
        std, ave = plot_image(image_path, theta, verbose=True)
        list_std_delta_result_float.append(std)
        list_ave_delta_result_float.append(ave)

    # plot the curve of std
    plt.plot(np.array(theta_list), np.array(list_std_delta_result_float))
    plt.plot(np.array(theta_list), np.array(list_std_delta_result_float), 's')
    plt.title(image_path.split('/')[-1] + '--std curve')
    plt.ylabel('std values')
    plt.xlabel('rotated angles')
    plt.savefig(image_path.replace('.jpeg', '_std_curve.jpeg'))
    plt.pause(0.5)
    plt.close()

    # plot the curve of ave
    plt.plot(np.array(theta_list), np.array(list_ave_delta_result_float))
    plt.plot(np.array(theta_list), np.array(list_ave_delta_result_float), 's')
    plt.title(image_path.split('/')[-1] + '--ave curve')
    plt.ylabel('ave values')
    plt.xlabel('rotated angles')
    plt.savefig(image_path.replace('.jpeg', '_ave_curve.jpeg'))
    plt.pause(0.5)
    plt.close()

    return True


if __name__ == "__main__":
    # list of the rotated angles
    theta_list = [-20, -15, -10, -5, -3, 3, 5, 10, 15, 20]

    # paths of the two images
    image1_path = r'\Users\milan\Desktop\DrZhang_20201009\Brain.jpeg'
    image2_path = r'\Users\milan\Desktop\DrZhang_20201009\GrayScaleImg.jpeg'

    # main functon
    plot_curve(theta_list, image1_path)
    plot_curve(theta_list, image2_path)
