import sys, traceback, Ice
import Mp3
import vlc
class LecteurMp3I(Mp3.LecteurMp3):

    def __init__(self):
	self.authorFile = None
	self.nameFile = None
	self.pathFile = None
	self.list_media = ["another.mp3", "punk.mp3","tiger.mp3","scotty.mp3","cortel", "melgroove.mp3"]
	self.media_name = "tiger.mp3"
	self.sout = '#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=:8090/'+ str(self.media_name)+'}';
	self.instance = vlc.Instance("")
	self.player = None

    def selectedMusic(self, name, current=None):
	self.media_name = name
	self.sout = '#transcode{acodec=mp3,ab=128,channels=2,samplerate=44100}:http{dst=:8090/'+ str(self.media_name)+'}';

    def getFilemp3(self, current=None):
	return self.list_media
    
    def jouer(self, current=None):
	try:
		self.instance.vlm_add_broadcast("test", self.media_name, self.sout, 0, None, True,False)
		#media=self.instance.media_new(self.media_name)
	except NameError:
		print ('NameError: % (%s vs Libvlc %s)' % (sys.exc_info()[1],vlc.__version__, vlc.libvlc_get_version()))
		sys.exit(1)
	self.instance.vlm_play_media("test")
	return 'http://192.168.1.53:8090/'+ str(self.media_name)
    
    def stop(self,current=None):
	self.instance.vlm_stop_media("test")

status = 0
ic = None
try:
    ic = Ice.initialize(sys.argv)
    adapter = ic.createObjectAdapterWithEndpoints("SimplePrinterAdapter", "default -p 10000 ")
    object = LecteurMp3I()
    adapter.add(object, ic.stringToIdentity("SimplePrinter"))
    adapter.activate()
    ic.waitForShutdown()
except:
    traceback.print_exc()
    status = 1

if ic:
    # Clean up
    try:
        ic.destroy()
    except:
        traceback.print_exc()
        status = 1

sys.exit(status)
