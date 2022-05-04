HELP_1 = """🇹🇷 <u>**Türkçe Sabit Komutlar:**</u>
/oynat - Müzik çalmak için bu komutu baz alın. 
/vplay veya /vizle - Video izlemek için bu komutları baz alın. 
/durdur - Çalan müziği duraklatın.
/devam - Duraklatılmış müziği devam ettirin.
/mute - Çalan müziğin sesini kapatın.
/unmute - Sessiz müziğin sesini açın.
/atla - Geçerli çalan müziği atlayın.
/son - Müzik çalmayı durdurun.
/shuffle - Sıraya alınmış çalma listesini rastgele karıştırır.
/bul - Müzik indirmeyi botun başlat bölümüne gönderir. 
/auth - Grubun AUTH LİSTESİ'ne bir kullanıcı ekleyin. 
/unauth - Bir kullanıcıyı grubun AUTH LİSTESİ'nden kaldırın. 
/deleteplaylist - Listenizdeki kayıtlı müzikleri silin.
/sira- Müzik Kuyruğu Listesi'ni kontrol edin.
🇹🇷 <u>**Grup Ayarları:**</u>
/settings - Satır içi düğmelerle tam bir grubun ayarlarını ayarlamak
1️⃣ Ayarlayabilirsiniz **Ses Kalitesi** sesli sohbette akış yapmak istiyorsanız.
2️⃣ Ayarlayabilirsiniz **Video Kalitesi** sesli sohbette akış yapmak istiyorsanız.
3️⃣ **Kimlik Doğrulama Kullanıcıları**:- Yönetici komutları modunu buradan herkes veya yalnızca yöneticiler olarak değiştirebilirsiniz. Grubunuzda bulunan herkes yönetici komutlarını kullanabilirse(like /skip, /stop etc)
4️⃣ **Oynatma Modu Ayarları** :  Oynatma komutları bölümüyle ilgili yardım alın.
5️⃣ **Temiz Mod:** Etkinleştirildiğinde, sohbetinizin temiz ve iyi kalmasını sağlamak için botun mesajlarını grubunuzdan 5 dakika sonra siler.
6️⃣ **Komut Temizle** : Etkinleştirildiğinde, Bot yürütülen komutlarını siler (/oynat, /durdur, /shuffle, /son etc) hemen.
✅ **<u>Admin Commands:</u>**
/pause - Pause the playing music.
/resume - Resume the paused music.
/mute - Mute the playing music.
/unmute - Unmute the muted music.
/skip - Skip the current playing music.
/stop - Stop the playing music.
/shuffle - Randomly shuffles the queued playlist.
✅ <u>**Specific Skip:**</u>
/skip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.
✅ <u>**Loop Play:**</u>
/loop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.
✅ <u>**Auth Users:**</u>
Auth Users can use admin commands without admin rights in your chat.
/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group."""


HELP_2 = """✅ <u>**Play Commands:**</u>
/play or /vplay [Music Name or Youtube/Spotify/Apple/Resso/SoundCloud Link] 
    - Bot will start playing your given query on voice chat.
/stream [m3u8 or index links] 
    - Stream live links on voice chats.
/channelplay [Channel Username or ID] or [linked] 
    - Connect channel to a group and stream music on channel's voice chat from your group. You need to be the **Owner** of the channel to connect it. Alternatively you can link your group to that channel and then try connnecting with `/channelplay linked`"
After connecting channel, change playmode to channel from group via /playmode
✅ <u>**Supported Platform:**</u> 
Bot only supports YouTube, AppleMusic, Spotify, Resso, Soundcloud, M3u8 and Index Links
✅ **<u>Bot's Server Playlists:</u>**
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
✅ <u>**Play Settings:**</u>
/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 
🔗 **Options in playmode:** [Get more info on clicking the button there]
1️⃣ **Search Mode** [ Direct or Inline] :- Changes your search mode while you give /play mode. 
2️⃣ **Play Mode** [ Group or Channel] :- Changes your Play mode to channel or group and streams music there only.
3️⃣ **Play Type** [ Everyone or Admins] :- If admins, only admins present in group can play music on voice chat."""


HELP_3 = """✅ <u>**Bot Commands:**</u>
/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.
/sudolist - Check Sudo Users of Yukki Music Bot
/lyrics [Music Name] - Searches Lyrics for the particular Music on web.
/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.
/queue- Check Queue List of Music."""


HELP_4 = """✅ <u>**Extra  Commands:**</u>
/start - Start the Yukki Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Yukki.
✅ <u>**Group Settings:**</u>
/settings - Get a complete group's settings with inline buttons
🔗 **Options in Settings:**
1️⃣ You can set **Audio Quality** you want to stream on voice chat.
2️⃣ You can set **Video Quality** you want to stream on voice chat.
3️⃣ **Auth Users**:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)
4️⃣ **Play Mode Settings** :  Get help regarding in play commands section.
5️⃣ **Clean Mode:** When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.
6️⃣ **Command Clean** : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately."""
