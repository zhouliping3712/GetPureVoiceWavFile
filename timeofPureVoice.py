
'''
   paras:
       songpath:带有路径的wav文件名;
       resultName:wav文件名
       
'''
def split_wav_file(k,wavfilePath,resultwavfilePath):
    if(os.path.getsize(wavfilePath)>0 and os.path.exists(wavfilePath)):
        wav = AudioSegment.from_wav(wavfilePath)
        chunks = split_on_silence(
    #            要加载的音频
                wav,
    #           规定每个静默块的长度，3000ms，即3s
                min_silence_len = 3000,
    #            静默的声呗阈值
                silence_thresh = -60
                )
        playList = AudioSegment.empty()
        for i,chunk in enumerate(chunks):
            normalized_chunk = chunk
            normalized_chunk.export(
            ".//chunks/chunk{0}.wav".format(k),
            bitrate = "192k",
            format = "wav"
            )
            song1 = AudioSegment.from_wav(".//chunks/chunk{0}.wav".format(k))
            playList = playList + song1
        playList.export(resultwavfilePath, format='wav')
        listInfo = [len(wav)/1000,len(playList)/1000]
        testInfo = [wavfilePath,os.path.getsize(wavfilePath),os.path.getsize(resultwavfilePath),len(wav)/1000,len(playList)/1000]
        saveDataframetoCsv(testInfo)
        return listInfo
    else:
        return [0,0]