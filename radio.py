from playsound import playsound
import threading
import pyaudio
import wave

class RecordThread(threading.Thread):
    def __init__(self, audiofile='record.wav'):
        threading.Thread.__init__(self)
        self.bRecord = True
        self.audiofile = audiofile
        self.chunk = 1024
        self.format = pyaudio.paInt16
        self.channels = 1 #单通道
        self.rate = 32000 #采样率为32000

    def run(self):
        audio = pyaudio.PyAudio()
        wavfile = wave.open(self.audiofile, 'wb')#打开文件，用二进制写模式
        wavfile.setnchannels(self.channels)
        wavfile.setsampwidth(audio.get_sample_size(self.format))
        wavfile.setframerate(self.rate)
        wavstream = audio.open(format=self.format, 
                               channels=self.channels,
                               rate=self.rate,
                               input=True,
                               frames_per_buffer=self.chunk)
        while self.bRecord:
            wavfile.writeframes(wavstream.read(self.chunk))
         
        #停止数据流
        wavstream.stop_stream()#文件写完之后跳出
        wavstream.close()#不要忘记关闭文件哦
        audio.terminate()#到这里就终止啦

    def stoprecord(self):
        self.bRecord = False

def main1():
    li = []
    x = input('请输入文件名')
    li.append(x)
    record = {x}
    RECORDS.append(record)
    for i in li:
        file_name = i + '.wav'
        audio_record = RecordThread(file_name)
        audio_record.start()#开始录音
        key = input("请按回车键结束录音,本次创建文件名" + i + ".wav")
        audio_record.stoprecord()#停止录音，调用参数变成False结束循环
        

def play1():
    h = input('请输入音频的文件名')
    playsound(h)

       
def main():
    print('='*30)
    print('1.开始录音')
    print('2.播放录音')
    print('3.退出')
    print('='*30)

    while True:
        option = input("请输入选项：")

        if option == '1':
            main1()
        elif option == '2':
            play1()

        elif option == '3':	
            break
        else:
            print("请输入正确的选项")
main() 