module Mp3{
	sequence<string> ItemMusicSeq;
	interface LecteurMp3{
		string jouer();
		string pause();
		void stop();
		void selectedMusic(string name);
		ItemMusicSeq getFilemp3();
		
	};
};
