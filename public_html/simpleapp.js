var lblNow, lblElapsed, lblRemain, lblInfo, panInfoOuter, btnStart, btnStop, btnReset, txtStopAt, txtCountdown, txtInfo, sound;
var mode = "stopAt", finished = false;
var startTimestamp, stopTimestamp;
var tmrUpdate, tmrNow;
var dist;

function Pad(n, width) {
    n += '';
    return n.length >= width ? n : new Array(width - n.length + 1).join('0') + n;
}

function GetFormattedDateTime(obj) {
    return Pad(obj.getFullYear(), 4) + "-" + Pad(obj.getMonth() + 1, 2) + "-" + Pad(obj.getDate(), 2) + " " +
        Pad(obj.getHours(), 2) + ":" + Pad(obj.getMinutes(), 2) + ":" + Pad(obj.getSeconds(), 2);
}

function tmrUpdate_Tick() {
    var now = new Date().getTime();
    var diff = now - startTimestamp.getTime();
    var remain = stopTimestamp.getTime() - now;

    if (remain <= 0) {
        clearInterval(updateTimer);
        remain = 0;
        diff = (stopTimestamp.getTime() - startTimestamp.getTime()) <= 0 ? 0 : stopTimestamp.getTime() - startTimestamp.getTime();
        finished = true;
        sound.play();
    }
    var hoursE = Math.floor(diff / (1000 * 60 * 60));
    diff -= hoursE * (1000 * 60 * 60);
    hoursE = Pad(hoursE, 2);

    var minsE = Math.floor(diff / (1000 * 60));
    diff -= minsE * (1000 * 60);
    minsE = Pad(minsE, 2);

    var secondsE = Math.floor(diff / 1000);
    diff -= secondsE * (1000);
    secondsE = Pad(secondsE, 2);


    var hoursR = Math.floor(remain / (1000 * 60 * 60));
    remain -= hoursR * (1000 * 60 * 60);
    hoursR = Pad(hoursR, 2);

    var minsR = Math.floor(remain / (1000 * 60));
    remain -= minsR * (1000 * 60);
    minsR = Pad(minsR, 2);

    var secondsR = Math.floor(remain / 1000);
    remain -= secondsR * (1000);
    secondsR = Pad(secondsR, 2);

    lblElapsed.innerHTML = hoursE + ":" + minsE + ":" + secondsE + "." + Pad(diff, 3);
    lblRemain.innerHTML = hoursR + ":" + minsR + ":" + secondsR + "." + Pad(remain, 3);
}

function btnStart_Click() {
    if (!finished) {
        if (startTimestamp == null)
            startTimestamp = new Date();
        if (stopTimestamp == null) {
            if (mode === "stopAt") {
                stopTimestamp = new Date(txtStopAt.value);
            }
            else {
                stopTimestamp = new Date(new Date().getTime() + Math.floor(txtCountdown.value * 60 * 1000));
            }
        }
        updateTimer = setInterval(tmrUpdate_Tick, 1);
    }
}

function btnStop_Click() {
    clearInterval(updateTimer);
}

function btnReset_Click() {
    btnStop_Click();
    startTimestamp = null;
    stopTimestamp = null;
    finished = false;
    lblElapsed.innerHTML = "--:--:--.---";
    lblRemain.innerHTML = "--:--:--:---";
}

function txtInfo_KeyUp() {
    lblInfo.innerHTML = txtInfo.value;
    var intResultSize;
    for (var intFontSize = 1; intFontSize < 100; intFontSize++) {
        lblInfo.style.fontSize = intFontSize;
        if (lblInfo.offsetHeight > panInfoOuter.offsetHeight) {
            intResultSize = intFontSize - 1;
            break;
        }
    }
    lblInfo.style.fontSize = intResultSize;
}

function txtStopAt_LostFocus() {
    if (mode == "stopAt") {
        var tmpDate = new Date(txtStopAt.value);
        if (!(d instanceof Date && !isNaN(d))) {
            alert("Invalid input, please make sure input looks like \"yyyy-mm-dd hh:mm(:ss)\"!");
        }
    }
}

function txtCountdown_LostFocus() {
    if (mode == "countDown") {
        var tmpDuration = txtCountdown.value;
        if (!(!isNaN(parseFloat(tmpDuration)) && isFinite(tmpDuration))) {
            alert("Invalid input, please make sure input is a decimal!");
        }
    }
}

function InitializeComponents() {
    lblNow = document.getElementById("lblNow");

    lblElapsed = document.getElementById("lblElapsed");

    lblRemain = document.getElementById("lblRemain");

    lblInfo = document.getElementById("lblInfo");

    btnStart = document.getElementById("btnStart");
    btnStart.onclick = btnStart_Click;

    btnStop = document.getElementById("btnStop");
    btnStop.onclick = btnStop_Click;

    btnReset = document.getElementById("btnReset");
    btnReset.onclick = btnReset_Click;

    var optTypeButtons = document.getElementsByName("optType");
    for (i = 0; i < optTypeButtons.length; ++i)
        optTypeButtons[i].onchange = function () {
            mode = this.value;
        };

    txtStopAt = document.getElementById("txtStopAt");
    txtStopAt.onblur = txtStopAt_LostFocus;
    txtStopAt.value = GetFormattedDateTime(new Date());

    txtCountdown = document.getElementById("txtCountdown");
    txtCountdown.onblur = txtCountdown_LostFocus;

    panInfoOuter = document.getElementById("panInfoOuter");

    txtInfo = document.getElementById("txtInfo");
    txtInfo.onkeyup = txtInfo_KeyUp;

    sound = document.getElementById("sound");

    tmrNow = setInterval(function () {
        lblNow.innerHTML = GetFormattedDateTime(new Date());
    }, 100);
}

function Window_Load() {
    console.log("LOAD");
    InitializeComponents();
}

window.onload = Window_Load;
