var display = document.getElementById('imgDiv');
var sound;

let currentEmotion = "neutral";
let animationData = {};

const display_source = new EventSource('/next-display')
const sound_source = new EventSource('/next-sound')
display_source.onopen = (e) => console.log('Connection requested')
sound_source.onopen = (e) => console.log('Connection requested')


let data = JSON.parse(msg.data);
//let data = { name: 'angry' };


console.log("received display data: ")
console.log(data["name"])

// ADD YOUR CODE REGARDING DISPLAY HERE 

var nextEmotion = data["name"]
switch (currentEmotion) {
    case 'neutral':
        switch (nextEmotion) {
            case 'angry':
                animationData = neutralToAngry;
                break;
            case 'fear':
                animationData = neutralToFear;
                break;
            case 'sad':
                animationData = neutralToSad;
                break;
            case 'affection':
                animationData = neutralToAffection;
                break;
            case 'curious':
                animationData = neutralToCurious;
                break;
            case 'sleepy':
                animationData = neutralToSleepy;
                break;
            case 'joy':
                animationData = neutralToJoy;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'fear':
        switch (nextEmotion) {
            case 'angry':
                animationData = fearToAngry;

                break;
            case 'neutral':
                animationData = fearToNeutral;
                break;
            case 'anger':
                animationData = fearToAngry;
                break;
            case 'affection':
                animationData = fearToAffection;
                break;
            case 'curious':
                animationData = fearToCurious;
                break;
            case 'sleepy':
                animationData = fearToSleepy;
                break;
            case 'joy':
                animationData = fearToJoy;
                break;
            case 'sad':
                animationData = fearToSad;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'angry':
        switch (nextEmotion) {
            case 'neutral':
                animationData = angryToNeutral;
                break;
            case 'fear':
                animationData = angryToFear;
                break;
            case 'affection':
                animationData = angryToAffection;
                break;
            case 'curious':
                animationData = angryToCurious;
                break;
            case 'sleepy':
                animationData = angryToSleepy;
                break;
            case 'joy':
                animationData = angryToJoy;
                break;
            case 'sad':
                animationData = angryToSad;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'affection':
        switch (nextEmotion) {
            case 'angry':
                animationData = affectionToAngry;
                break;
            case 'neutral':
                animationData = {};
                break;
            case 'fear':
                animationData = affectionToFear;
                break;
            case 'curious':
                animationData = affectionToCurious;
                break;
            case 'sleepy':
                animationData = affectionToSleepy;
                break;
            case 'joy':
                animationData = affectionToJoy;
                break;
            case 'sad':
                animationData = affectionToSad;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'curious':
        switch (nextEmotion) {
            case 'angry':
                animationData = curiousToAngry;
                break;
            case 'neutral':
                animationData = curiousToNeutral;
                break;
            case 'fear':
                animationData = curiousToFear;
                break;
            case 'anger':
                animationData = curiousToAnger;
                break;
            case 'affection':
                animationData = curiousToAffection;
                break;
            case 'sleepy':
                animationData = curiousToSleepy;
                break;
            case 'joy':
                animationData = curiousToJoy;
                break;
            case 'sad':
                animationData = curiousToSad;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'sleepy':
        switch (nextEmotion) {
            case 'angry':
                animationData = sleepyToAngry;
                break;
            case 'neutral':
                animationData = sleepyToNeutral;
                break;
            case 'fear':
                animationData = sleepyToFear;
                break;
            case 'anger':
                animationData = sleepyToAnger;
                break;
            case 'affection':
                animationData = sleepyToAffection;
                break;
            case 'curious':
                animationData = sleepyToCurious;
                break;
            case 'joy':
                animationData = sleepyToJoy;
                break;
            case 'sad':
                animationData = sleepyToSad;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'sad':
        switch (nextEmotion) {
            case 'angry':
                animationData = sadToAngry;
                break;
            case 'neutral':
                animationData = sadToNeutral;
                break;
            case 'fear':
                animationData = sadToFear;
                break;
            case 'affection':
                animationData = sadToAffection;
                break;
            case 'curious':
                animationData = sadToCurious;
                break;
            case 'joy':
                animationData = sadToJoy;
                break;
            case 'sleepy':
                animationData = sadToSleepy;
            default:
                console.log("no new emotion to display");
        }
        break;
    case 'joy':
        switch (nextEmotion) {
            case 'angry':
                animationData = joyToAngry;
                break;
            case 'neutral':
                animationData = joyToNeutral;
                break;
            case 'fear':
                animationData = joyToFear;
                break;
            case 'sad':
                animationData = joyToSad;
                break;
            case 'affection':
                animationData = joyToAffection;
                break;
            case 'curious':
                animationData = joyToCurious;
                break;
            case 'sleepy':
                animationData = joyToSleepy;
                break;
            default:
                console.log("no new emotion to display");
        }
        break;
}
    var params = {
        container: document.getElementById('bodymovin'),
        renderer: 'svg',
        loop: true,
        autoplay: true,
        animationData: animationData
    };

    currentEmotion = nextEmotion;
    var params = {
        container: document.getElementById('bodymovin'),
        renderer: 'svg',
        loop: false,
        autoplay: true,
        animationData: animationData
    };
    bodymovin.destroy();
    var anim;
    anim = bodymovin.loadAnimation(params);


    let url = 'audio/' + currentEmotion + '_01.wav';
    sound = new Audio(url);
    let now = Date.now(),
        end = now + 2000;
    while (now < end) { now = Date.now(); }
    sound.play();

/* display_source.onmessage = (msg) => {
     try {
} catch (error) {
 console.error('Wrong message type', error);
}
}*/

/*sound_source.onmessage = (msg) => {
    try {
        let data = JSON.parse(msg.data)

        console.log("received sound data: ")
        console.log(data)

        if (currentEmotion) {
            if (sound) {
                sound.pause();
                sound.currentTime = 0;
            }
            let url = './audio/' + currentEmotion + '_01.wav';
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
}*/

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