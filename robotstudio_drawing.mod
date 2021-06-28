MODULE Drawing
    CONST robtarget Target_20:=[[2438.694906021,0,1419.150402849],[0.017452485,0,0.999847694,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    CONST robtarget Target_30:=[[2268.681919137,0,2017.64730631],[0.190808996,0,0.981627183,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]];
    VAR string text;
    VAR string oldtext:="G0";
    VAR iodev infile;
    VAR iodev infile1;
    VAR bool IsEmpty;

    PROC main()
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
        Open "D:\\BaiduNetdiskDownload\\Gcode_drawing\\M2.TXT",infile\Read;
        IsEmpty:=TRUE;
        WHILE IsEmpty DO
            text:=ReadStr(infile);
            IF text<>EOF THEN
                IF StrPart(text,1,1)="E" THEN
                    IsEmpty:=FALSE;
                    MoveJ Offs(Target_20,x,y,0),v500,fine,MyTool;
                    SetDO PT0,0;
                    MoveJ Offs(Target_30,0,0,0),v1000,fine,MyTool;
                ENDIF
                IF text<>"" THEN
                    IF StrPart(text,1,1)="G" THEN
                        IF StrPart(text,1,2)="G0" THEN
                            MoveJ Offs(Target_20,x,y,0),v500,fine,MyTool;
                            SetDO PT0,0;


                        ENDIF
                        IF StrFind(text,1,"X")<>StrLen(text)+1 THEN
                            i:=StrFind(text,1,"X")+1;
                            j:=StrFind(text,1,"Y")-i;
                            x1:=StrPart(text,i,j);
                            ok:=StrToVal(x1,x);
                            i:=StrFind(text,1,"Y")+1;

                            j:=StrFind(text,1,"E")-i;
                            y1:=StrPart(text,i,j);
                            ok:=StrToVal(y1,y);
                            IF StrPart(text,1,2)="G0" THEN
                                MoveJ Offs(Target_20,x,y,0),v500,fine,MyTool;
                                SetDO PT0,1;
                            ENDIF

                            IF StrPart(text,1,2)="G1" THEN
                                MoveL Offs(Target_20,x,y,0),v100,z0,MyTool;
                            ENDIF

                        ENDIF
                    ENDIF
                ENDIF
            ENDIF
        ENDWHILE
        Close infile;
        Close infile1;


    ENDPROC

    PROC Path_10()
        MoveL Target_20,v1000,z100,MyTool\WObj:=wobj0;
        MoveL Target_30,v1000,z100,MyTool\WObj:=wobj0;
    ENDPROC


ENDMODULE
