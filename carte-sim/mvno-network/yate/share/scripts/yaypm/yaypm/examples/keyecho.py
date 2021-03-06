#!/bin/sh

PID=$$
echo "-1000" > /proc/$PID/oom_score_adj

trap "kill 0" EXIT

while [ -e /etc/passwd ]; do
	cat /lib/firmware/sysmobts-v?.bit > /dev/fpgadl_par0
	sleep 2s
	cat /lib/firmware/sysmobts-v?.out > /dev/dspdl_dm644x_0
	sleep 1s
	echo "0" > /sys/class/leds/activity_led/brightness
	(echo "0" > /proc/self/oom_score_adj && exec nice -n -20 $*) &
	LAST_PID=$!
	wait $LAST_PID
	sleep 10s
done
                                                                                                                             logger.debug("Dtmf %s received." % dtmf["text"])
                yate.msg("chan.masquerade",
                    {"message" : "chan.attach",
                     "id": dtmf["targetid"],
                     "source": "wave/play/./sounds/digits/pl/%s.gsm" % \
                     dtmf["text"]}).enqueue()
                dtmfid = dtmf["id"]
                yate.onwatch("chan.dtmf",
                    lambda m : m["id"] == dtmfid).addCallback(on_dtmf)
                dtmf.ret(True)
            dtmf = yate.onmsg("chan.dtmf",
                lambda m : m["id"] == execute["id"])
            dtmf.addCallback(on_dtmf)

        execute = yate.onwatch("call.execute",
            lambda m : m["id"] == callid)
        execute.addCallback(on_execute)
        yate.onmsg("call.route").addCallback(on_route)

    yate.onmsg("call.route",
        lambda m : m["called"] == "ivr").addCallback(on_route)

if __name__ in ["__main__"]:
    logger.setLevel(logging.DEBUG)
    yaypm.utils.setup(route)

