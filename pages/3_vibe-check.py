import streamlit as st

def mood_recommender():
    st.title("🎬 Mood-Based Video Recommender")
    st.write("Pick your mood and explore a feed of YouTube videos curated for you ✨")

    # Mood selection
    mood = st.selectbox(
        "How are you feeling right now?",
        ["Happy", "Sad", "Stressed", "Relaxed", "Low Motivated", "Angry"]
    )

    # Dictionary of moods → list of videos (id, title, channel)
    videos = {
        "Happy": [
            {"id": "ZbZSe6N_BXs", "title": "Pharrell Williams - Happy", "channel": "Pharrell Williams"},
            {"id": "kJQP7kiw5Fk", "title": "Luis Fonsi - Despacito ft. Daddy Yankee", "channel": "Luis Fonsi"},
            {"id": "9bZkp7q19f0", "title": "PSY - GANGNAM STYLE", "channel": "officialpsy"},
            {"id": "3JZ_D3ELwOQ", "title": "Mark Ronson - Uptown Funk ft. Bruno Mars", "channel": "Mark Ronson"},
            {"id": "hT_nvWreIhg", "title": "OneRepublic - Counting Stars", "channel": "OneRepublic"},
            {"id": "fJ9rUzIMcZQ", "title": "Queen – Bohemian Rhapsody", "channel": "Queen Official"},
            {"id": "60ItHLz5WEA", "title": "Alan Walker - Faded", "channel": "Alan Walker"},
            {"id": "ktvTqknDobU", "title": "Imagine Dragons - Radioactive", "channel": "Imagine Dragons"},
            {"id": "2Vv-BfVoq4g", "title": "Ed Sheeran - Perfect", "channel": "Ed Sheeran"},
            {"id": "tt2k8PGm-TI", "title": "The Chainsmokers & Coldplay - Something Just Like This", "channel": "ChainsmokersVEVO"},
        ],
        "Sad": [
            {"id": "RB-RcX5DS5A", "title": "Coldplay - Fix You", "channel": "Coldplay"},
            {"id": "uelHwf8o7_U", "title": "Eminem - Love The Way You Lie ft. Rihanna", "channel": "EminemVEVO"},
            {"id": "hLQl3WQQoQ0", "title": "Adele - Someone Like You", "channel": "Adele"},
            {"id": "YVkUvmDQ3HY", "title": "Eminem - Stan", "channel": "EminemVEVO"},
            {"id": "RgKAFK5djSk", "title": "Wiz Khalifa - See You Again ft. Charlie Puth", "channel": "Wiz Khalifa"},
            {"id": "JkK8g6FMEXE", "title": "James Blunt - Goodbye My Lover", "channel": "James Blunt"},
            {"id": "4N3N1MlvVc4", "title": "Johnny Cash - Hurt", "channel": "Johnny Cash"},
            {"id": "io1ps1ked4E", "title": "Linkin Park - In The End", "channel": "Linkin Park"},
            {"id": "kOkQ4T5WO9E", "title": "Lewis Capaldi - Someone You Loved", "channel": "Lewis Capaldi"},
            {"id": "8UVNT4wvIGY", "title": "Gotye - Somebody That I Used To Know", "channel": "Gotye"},
        ],
        "Stressed": [
            {"id": "2OEL4P1Rz04", "title": "Relaxing Piano Music", "channel": "Relax Music"},
            {"id": "2oY0k-c7WNo", "title": "10 Hours of Relaxing Rain Sounds", "channel": "Rain Sounds"},
            {"id": "lFcSrYw-ARY", "title": "Peaceful Meditation Music", "channel": "Soothing Relaxation"},
            {"id": "jfKfPfyJRdk", "title": "lofi hip hop radio - beats to relax/study to", "channel": "Lofi Girl"},
            {"id": "DWcJFNfaw9c", "title": "Deep Focus Music", "channel": "Chillhop Music"},
            {"id": "Ml4N4O1wb9Y", "title": "Calm Nature Sounds", "channel": "Nature Healing Society"},
            {"id": "OdIJ2x3nxzQ", "title": "Gentle Ocean Waves", "channel": "SleepDroid Studios"},
            {"id": "kp2N-Uuwx9o", "title": "Yoga Meditation Music", "channel": "PowerThoughts Meditation Club"},
            {"id": "vPhg6sc1Mk4", "title": "Forest Ambience with Birds", "channel": "Relaxing White Noise"},
            {"id": "I7LMmRzkOaM", "title": "Soothing Flute Meditation", "channel": "Peaceful Mind"},
        ],
        "Relaxed": [
            {"id": "jfKfPfyJRdk", "title": "lofi hip hop radio - beats to relax/study to", "channel": "Lofi Girl"},
            {"id": "2OEL4P1Rz04", "title": "Relaxing Piano Music", "channel": "Relax Music"},
            {"id": "lFcSrYw-ARY", "title": "Peaceful Meditation Music", "channel": "Soothing Relaxation"},
            {"id": "DWcJFNfaw9c", "title": "Deep Focus Music", "channel": "Chillhop Music"},
            {"id": "2oY0k-c7WNo", "title": "Rain Sounds for Relaxation", "channel": "Rain Sounds"},
            {"id": "kp2N-Uuwx9o", "title": "Yoga Music for Relaxing", "channel": "PowerThoughts Meditation Club"},
            {"id": "OdIJ2x3nxzQ", "title": "Ocean Waves for Sleep", "channel": "SleepDroid Studios"},
            {"id": "Ml4N4O1wb9Y", "title": "Calm Nature Sounds", "channel": "Nature Healing Society"},
            {"id": "I7LMmRzkOaM", "title": "Soothing Flute Music", "channel": "Peaceful Mind"},
            {"id": "vPhg6sc1Mk4", "title": "Forest Ambience with Birds", "channel": "Relaxing White Noise"},
        ],
        "Low Motivated": [
            {"id": "mgmVOuLgFB0", "title": "Best Motivational Speech Compilation", "channel": "MotivationHub"},
            {"id": "wnHW6o8WMas", "title": "NEVER GIVE UP - Motivational Video", "channel": "Ben Lionel Scott"},
            {"id": "ZXsQAXx_ao0", "title": "Dream - Motivational Video", "channel": "Mateusz M"},
            {"id": "26U_seo0a1g", "title": "Believe in Yourself - Motivational Video", "channel": "Absolute Motivation"},
            {"id": "sZ4f5xW3p1M", "title": "Hard Work Pays Off", "channel": "Eric Thomas"},
            {"id": "mgmVOuLgFB0", "title": "Rise & Grind - Motivation", "channel": "MotivationHub"},
            {"id": "H14bBuluwB8", "title": "Why Do We Fall? - Motivational Video", "channel": "Mateusz M"},
            {"id": "mgmVOuLgFB0", "title": "The Mindset of High Achievers", "channel": "MotivationHub"},
            {"id": "ZXsQAXx_ao0", "title": "Push Through Pain", "channel": "Ben Lionel Scott"},
            {"id": "wnHW6o8WMas", "title": "Success Requires Sacrifice", "channel": "Absolute Motivation"},
        ],
        "Angry": [
            {"id": "lFcSrYw-ARY", "title": "Peaceful Meditation Music", "channel": "Soothing Relaxation"},
            {"id": "2OEL4P1Rz04", "title": "Relaxing Piano Music", "channel": "Relax Music"},
            {"id": "jfKfPfyJRdk", "title": "lofi hip hop radio - beats to relax/study to", "channel": "Lofi Girl"},
            {"id": "2oY0k-c7WNo", "title": "10 Hours of Rain Sounds", "channel": "Rain Sounds"},
            {"id": "DWcJFNfaw9c", "title": "Deep Focus Music", "channel": "Chillhop Music"},
            {"id": "OdIJ2x3nxzQ", "title": "Ocean Waves for Relaxation", "channel": "SleepDroid Studios"},
            {"id": "Ml4N4O1wb9Y", "title": "Calm Nature Sounds", "channel": "Nature Healing Society"},
            {"id": "vPhg6sc1Mk4", "title": "Forest Ambience with Birds", "channel": "Relaxing White Noise"},
            {"id": "kp2N-Uuwx9o", "title": "Yoga Meditation Music", "channel": "PowerThoughts Meditation Club"},
            {"id": "I7LMmRzkOaM", "title": "Flute Meditation for Calmness", "channel": "Peaceful Mind"},
        ]
    }

    st.markdown(f"### 🎥 Recommended for your mood: *{mood}*")

    # Render video cards
    for video in videos[mood]:
        col1, col2 = st.columns([1.2, 3])

        with col1:
            thumbnail_url = f"https://img.youtube.com/vi/{video['id']}/hqdefault.jpg"
            st.image(thumbnail_url, use_container_width=True)
            st.markdown(
                f"[▶️ Watch](https://www.youtube.com/watch?v={video['id']})",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(f"**{video['title']}**")
            st.caption(f"📺 {video['channel']}")
        st.divider()  # horizontal line like YouTube

    return mood


if __name__ == "__main__":
    mood_recommender()
