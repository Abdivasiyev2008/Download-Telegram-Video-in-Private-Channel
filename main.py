from telethon.sync import TelegramClient

api_id = #2423423
api_hash = # '234234234gr2432423'


def list_channels():
    with TelegramClient('session_name', api_id, api_hash) as client:
        client.start()
        dialogs = client.get_dialogs()

        for i, dialog in enumerate(dialogs, start=1):
            if dialog.is_channel:
                print(f"{i}. {dialog.name} - {dialog.id}")

def access_channel(channel_id):
    with TelegramClient('session_name', api_id, api_hash) as client:
        client.start()
        try:
            channel = client.get_entity(int(channel_id))
            print(f"Kanaldagi videolarni yuklash uchun {channel.title} kanaliga muvaffaqiyatli kirildi.")
            return channel
        except ValueError as e:
            print(f"Xatolik yuz berdi: {e}")
            return None

def download_video(channel_username, video_id):
    channel = access_channel(channel_username)
    if channel:
        with TelegramClient('session_name', api_id, api_hash) as client:
            try:
                messages = client.get_messages(channel, ids=[int(video_id)])
                for message in messages:
                    if message.media and hasattr(message.media, 'document'):
                        client.download_media(message.media.document, file='./videolar/{}.mp4'.format(video_id))
                        print('Videoni yuklab olish muvaffaqiyatli amalga oshirildi.')
                        return
                    
                print('Videoni yuklab olish muvaffaqiyatsiz amalga oshirildi.')
                
            except ValueError as e:
                print(f"Xatolik yuz berdi: {e}")

list_channels()
selected_channel = input("Tanlangan kanal username'ini kiriting: ")
video_id = input("Kanalda mavjud bo'lgan videoning ID sini kiriting: ")

download_video(selected_channel, video_id)