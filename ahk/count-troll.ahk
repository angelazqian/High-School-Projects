z::
x := 0
Loop, 5000
{
	Random, x, 1, 6
	if (x == 2)
	{
		send \"It's muskrat time\" - Elon Musk 2022
		send, {Enter}
		sleep %1000%
	}
	if (x == 3)
	{
		send \"The depths of discord must feel despair as well\" - Elon Musk 2022
		send, {Enter}
		sleep %1000%
	}
	Random, x, 25000, 100000
	MouseMove, x/100, x/100
	send %x%
	send, {Enter}
	Random, x, 0, 547
	x := x**(2)
	x += 900000 
	sleep %x%
}
Esc::ExitApp
