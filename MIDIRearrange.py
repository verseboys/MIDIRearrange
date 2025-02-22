#########################################################
####    Ver1.2.2 @ 20250222
####    Ver1.2.1 @ 20240108 Happy Birthday Coding
####    Ver1.2 @ 20230527
####    Ver1.1 @ 20230510
####    Ver1.0 @ 20230119
####    Author:Roye
#########################################################
#!/usr/bin/python
#-- coding:utf8 --
from mido import MidiFile,Message,MidiTrack
import os
import traceback

def midiRearrange_cmd_main():
    import argparse
    # 设置参数名
    parser = argparse.ArgumentParser()
    # parser.add_argument("-i", dest="midifile", type=str, default=path.name,help='input midifile path')
    # parser.add_argument("-i", dest="midifile", type=str, default='')
    parser.add_argument("-v", dest="velocity", type=int, default='30',help='default 30, less than this value will be removed')
    parser.add_argument("-t", dest="timespan", type=int, default='20',help='default 20, less than this value will be removed')
    parser.add_argument("-s", dest="separate", type=int, default='50',help='default 50, gap between different note_on less than this value will be regarded as strike in the same time')
    parser.add_argument("-c", dest="continue_note", type=int, default='100',help='default 100, gap between the same note_on will be regarded as one')

    # 获取参数
    args = parser.parse_args()

    velocity_threshold = args.velocity #30 #响度阈值
    timeSpan_threshold = args.timespan #20 #持续时间阈值(按下立刻抬起的事件)
    separate_threshold = args.separate #80 #琶音整合阈值
    continue_threshold = args.continue_note

    print ('velocity_threshold:',velocity_threshold)
    print ('timeSpan_threshold:',timeSpan_threshold)
    print ('separate_threshold:',separate_threshold)
    print ('continue_threshold:',continue_threshold)

    from tkinter import filedialog
    path = filedialog.askopenfile()
    # 传参方式
    #python test.py -i test.mid
    if(path is None or path.name == ''):
        print ('\r\nPlease select correct MIDI(.mid) file\r\n')
        return None
    try:
        timeSpan_threshold,separate_threshold,_ = param_check(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path.name)
        midiRearrange(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path.name)
    except Exception as e:
        print (traceback.print_exc())

def param_check(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path):
    msg_list = []
    mid = MidiFile(path)#('tothemoon.mid')
    if(mid.ticks_per_beat != 384):
        if(timeSpan_threshold==20 and separate_threshold==50):
            
            msg_list.append("参考midi节拍数为384")
            msg_list.append(f"当前midi节拍数为{mid.ticks_per_beat}")
            msg_list.append("检测到当前未更改时间相关参数，且由于曲速问题可能导致异常，将自动按比例缩放参数并进行处理... ...")
            timeSpan_threshold = round(timeSpan_threshold*mid.ticks_per_beat/384)
            separate_threshold = round(separate_threshold*mid.ticks_per_beat/384)
            msg_list.append('自动处理后参数:')
            msg_list.append(f'velocity_threshold:{velocity_threshold}')
            msg_list.append(f'timeSpan_threshold:{timeSpan_threshold}')
            msg_list.append(f'separate_threshold:{separate_threshold}')
            msg_list.append(f'continue_threshold:{continue_threshold}')
            print(msg_list)
    return timeSpan_threshold,separate_threshold,msg_list


def midiRearrange(velocity_threshold,timeSpan_threshold,separate_threshold,continue_threshold,path):
    try:
        mid = MidiFile(path)#('tothemoon.mid')
        newmid =  MidiFile()
        track = MidiTrack()

        onnote = 0
        offnote = 0
        timeline = 0
        onList = []
        pretype = ''

        newmid.ticks_per_beat = mid.ticks_per_beat
        #ticks_per_beat 384
        onnote_dict = {}

        tracknum = 1
        try:
            mid.tracks[tracknum]
            newmid.tracks.append(mid.tracks[0])
        except:
            tracknum = 0 
        # 提取按下
        for ttrack in mid.tracks[tracknum]:

            if (ttrack.type=='control_change'):

                timeline += ttrack.time

            elif (ttrack.type=='note_on' or ttrack.type=='note_off'):
                timeline += ttrack.time

                if(ttrack.velocity>velocity_threshold):
                    onnote = ttrack.note

                    if(onnote in onnote_dict and timeline - onnote_dict[onnote] < continue_threshold and ttrack.velocity< 2*velocity_threshold):
                        onnote_dict[onnote] = timeline
                        continue
                    
                    onnote_dict[onnote] = timeline
                    pretype = 'on'
                    ttrack.time = timeline
                    track.append(ttrack)
                    
                if(ttrack.velocity == 0 or ttrack.type=='note_off'):
                    offnote = ttrack.note
                    if(pretype=='on' and onnote == offnote and ttrack.time < timeSpan_threshold):
                        del track[len(track)-1]
                    pretype = 'off'
            # else:
            #     print ('what?')

        #整和琶音
        timeline = 0
        pretime = 0
        for ttrack in track:
            if(ttrack.time-timeline > separate_threshold):
                timeline = ttrack.time
                pretime = ttrack.time
            else:
                timeline = ttrack.time
                ttrack.time = pretime


        #分离事件
        newtrack = MidiTrack()
        pretime = 0
        keyArea = 1
        #for i in range (0,len(track),1):
        for ttrack in track:
            #ttrack = track[i]
            if(ttrack.time > pretime):#新按下
                pretime = ttrack.time

                if(ttrack.note>=60):#高音区
                    keyArea = 1
                else:
                    keyArea = 0

                #for j in range (len(onList),0,-1):
                for onnote in onList[::-1]:
                    #onnote = onList[j]
                    #if((onnote >= 60 and keyArea == 1) or (onnote < 60 and keyArea == 0) ):
                    newtrack.append(Message('note_off', channel=0, note=onnote, velocity=0, time=ttrack.time-int(timeSpan_threshold*2)))
                    onList.remove(onnote)
                #onList = []
            onList.append(ttrack.note)
            newtrack.append(ttrack)

        #整理时间线
        timeline = 0
        pretime = 0
        for ttrack in newtrack:
            if (ttrack.type=='note_on' or ttrack.type=='note_off'):
                if(ttrack.time>timeline):
                    timeline = ttrack.time
                    ttrack.time = ttrack.time-pretime
                    pretime = timeline
                else:
                    ttrack.time = ttrack.time-timeline
                # if(ttrack.time ==0):
                #     ttrack.time = 1

        #补全结束
        for onnote in onList[::-1]:
            newtrack.append(Message('note_off', channel=0, note=onnote, velocity=0, time=2000))

        newmid.tracks.append(newtrack)
        outputfilename = path+'Rearrange.mid'
        return_msg = f'\r\nRearrange Success!\r\nOutputFile:{outputfilename}'
        print(return_msg)
        newmid.save(outputfilename)
        return return_msg
    except Exception as e:
        return_msg = f'\r\nRearrange Failed!\r\nError:{traceback.print_exc()}'
        print(return_msg)
        return return_msg
    
if __name__=="__main__":
    midiRearrange_cmd_main()
    os.system("pause")