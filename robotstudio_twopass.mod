MODULE one_pass


    PROC onepass()
        VAR bool ok;
        VAR num x:=0;
        VAR num y:=0;
        VAR num oldx:=0;
        VAR num oldy:=0;
        VAR string x1:="0";
        VAR string y1:="0";
        VAR num i:=0;
        VAR num j:=0;
        VAR num jojo:=1;

        Open "C:\\MI.TXT",infile\Read;
        Open "C:\\MOKO.TXT",infile1\Write;
        IsEmpty:=TRUE;

        WHILE IsEmpty DO
            text:=ReadStr(infile);

            IF text<>"" THEN
                IF strpart(text,1,1)="E" THEN
                    IsEmpty:=FALSE;
                ENDIF


                IF text<>"" THEN
                    IF strpart(text,1,1)="G" THEN
                        IF strfind(text,1,"X")<>strLen(text)+1 THEN
                            i:=strfind(text,1,"X")+1;
                            j:=strfind(text,1,"Y")-i;
                            x1:=strpart(text,i,j);
                            ok:=strtoval(x1,x);
                            i:=strfind(text,1,"Y")+1;

                            j:=strfind(text,1,"E")-i;
                            y1:=strpart(text,i,j);
                            ok:=strtoval(y1,y);




                            IF strpart(text,1,2)="G1" THEN
                                IF strpart(oldtext,1,2)="G0" THEN

                                    Write infile1,oldtext;

                                ENDIF

                                IF Sqrt((x-oldx)*(x-oldx)+(y-oldy)*(y-oldy))>1 THEN
                                    Write infile1,"G1  X"+ValToStr(x)+"   Y"+ValToStr(y);
                                    oldx:=x;
                                    oldy:=y;


                                ENDIF

                            ENDIF

                        ENDIF

                    ENDIF


                    oldtext:=text;

                ENDIF


            ENDIF



        ENDWHILE
        Close infile;
        Close infile1;

    ENDPROC


ENDMODULE