var display = document.getElementById('imgDiv');
var sound;
console.log("test in script");

const display_source = new EventSource('/next-display')
const sound_source = new EventSource('/next-sound')
display_source.onopen = (e) => console.log('Connection requested')
sound_source.onopen = (e) => console.log('Connection requested')

display_source.onmessage = (msg) => {
    try {
        console.log('inside onload function');
        let data = JSON.parse(msg.data)

        //TEST DATA
        //let currentEmotion = 'neutral';
        //let data = { 'name': 'joy' }
        console.log("received display data: ")
        console.log(data)

        // ADD YOUR CODE REGARDING DISPLAY HERE 
        /*hol emotion feld, ruf funktion mit switch case mit emotion von data field AudioBuffer, bekomme animation data zurück, füge diese in richtiges html element ein
        bei sound filename oder so */

        var nextEmotion = data["name"]
        lottie.unfreeze();
        switch (currentEmotion) {
            case neutral:
                switch (nextEmotion) {
                    case angry:
                        animationData = neutralToAngry;
                        // setTimeout(3000);
                        // lottie.freeze();
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = neutralToJoy;
                        // setTimeout(3000);
                        // lottie.freeze();
                        break;
                    default: ("no emotion to display");

                }
                break;
            case fear:
                switch (nextEmotion) {
                    case angry:
                        animationData = fearToAngry;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = fearToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
            case anger:
                switch (nextEmotion) {
                    case angry:
                        animationData = angerToSad;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = angerToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
            case affection:
                switch (nextEmotion) {
                    case angry:
                        animationData = affectionToAngry;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = affectionToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
            case curious:
                switch (nextEmotion) {
                    case angry:
                        animationData = curiousToAngry;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = curiousToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
            case sleepy:
                switch (nextEmotion) {
                    case angry:
                        animationData = sleepyToAngry;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = sleepyToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
            case joy:
                switch (nextEmotion) {
                    case angry:
                        animationData = joyToAngry;
                        break;
                    case sad:
                        animationData = {};
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
                    case joy:
                        animationData = neutralToJoy;
                        break;
                    default: ("no emotion to display");

                }
                break;
        }

        currentEmotion = nextEmotion;


    }



    /* OLD DATA (CAN BE DELETED)
    data = {
        "name": "Happy_face"
    }
 
    var name = data ["name"]
 
 
    if (data.display) {
        // Update gifs/pics
        display.innerHTML = '<img src=\'static/display/' + data.display + '\'>' //so ähnlich machen, in html unter templates svg definieren das aktuell leer ist, "javascript svg change data" googlen
    }
    // Stop previous Sound            
    if (sound) {
        sound.pause();
        sound.currentTime = 0;
    }
    // Load and start new sound
    einfügen in zeile 63
    if (data.audio) {
        let url = 'static/audio/' + data.audio;
        sound = new Audio(url);
        sound.play();
    }
    if(data.info) {
        console.log(data.info)
    } */


    catch (error) {
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
            let url = 'static/audio/' + fileName +'.wav';
            sound = new Audio(url);
            sound.play();
        }

    } catch (error) {
        console.error('Wrong message type', error);
    }
}

function isPlaying() { return !audio.paused; }

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

