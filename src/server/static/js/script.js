var display = document.getElementById('imgDiv');
var sound;

const display_source = new EventSource('/next-display')
const sound_source = new EventSource('/next-sound')
display_source.onopen = (e) => console.log('Connection requested')
sound_source.onopen = (e) => console.log('Connection requested')

display_source.onmessage = (msg) => {
    try {
        //let data = JSON.parse(msg.data)
        let currentEmotion = 'neutral';ahh
        let data = {name: 'angry'};

        console.log("received display data: ")
        console.log(data["name"])

        // ADD YOUR CODE REGARDING DISPLAY HERE 

        var nextEmotion = data["name"]
        switch (currentEmotion) {
            case neutral:
                switch (nextEmotion) {
                    case angry:
                        animationData = neutralToAngry;
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    case joy:
                        animationData = neutralToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case fear:
                switch (nextEmotion) {
                    case angry:
                        animationData = fearToAngry;
                        break;
                    case neutral:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    case joy:
                        animationData = fearToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case angry:
                switch (nextEmotion) {
                    case neutral:
                        animationData = {};
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    case joy:
                        animationData = angerToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case affection:
                switch (nextEmotion) {
                    case angry:
                        animationData = affectionToAngry;
                        break;
                    case neutral:
                        animationData = {};
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    case joy:
                        animationData = affectionToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case curious:
                switch (nextEmotion) {
                    case angry:
                        animationData = curiousToAngry;
                        break;
                    case neutral:
                        animationData = {};
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    case joy:
                        animationData = curiousToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case sleepy:
                switch (nextEmotion) {
                    case angry:
                        animationData = sleepyToAngry;
                        break;
                    case neutral:
                        animationData = {};
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case joy:
                        animationData = sleepyToJoy;
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
            case joy:
                switch (nextEmotion) {
                    case angry:
                        animationData = joyToAngry;
                        break;
                    case neutral:
                        animationData = {};
                        break;
                    case fear:
                        animationData = {};
                        break;
                    case anger:
                        animationData = {};
                        break;
                    case affection:
                        animationData = {};
                        break;
                    case curious:
                        animationData = {};
                        break;
                    case sleepy:
                        animationData = {};
                        break;
                    default:
                        console.log("no new emotion to display");
                }
                break;
        }

        currentEmotion = nextEmotion;
    } catch (error) {
        console.error('Wrong message type', error);
    }
}

sound_source.onmessage = (msg) => {
    try {
        let data = JSON.parse(msg.data)

        console.log("received sound data: ")
        console.log(data)

        var fileName = data["name"]

        if (fileName) {
            if (sound) {
                sound.pause();
                sound.currentTime = 0;
            }
            let url = 'static/audio/' + fileName + '.wav';
            sound = new Audio(url);
            sound.play();
        }



        // ADD YOUR CODE REGARDING SOUND HERE 

    } catch (error) {
        console.error('Wrong message type', error);
    }
}

function isPlaying() {
    return !audio.paused;
}

// Stopp audio and close sse connection on reload
window.onbeforeunload = (e) => {
    if (sound) {
        sound.pause();
        sound.currentTime = 0;
    }
    if (display_source.readyState == display_source.OPEN) {
        display_source.close();
    }
    if (sound_source.readyState == sound_source.OPEN) {
        sound_source.close();
    }
}

display_source.onerror = (error) => {
    console.error("connection disrupted", error);
}
sound_source.onerror = (error) => {
    console.error("connection disrupted", error);
}