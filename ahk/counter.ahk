z::
x := 1


while (x <= 69420)
{
send %x%
send, {Enter}
sleep 100
good := 1
count := 1
while (good = 1 && x!=100)
{
	PixelSearch , px, py, 595, 856, 628, 891 ,0x77b255,20,RGB
	if (ErrorLevel=0)
		good := 0
	else
	{
		count += 1
	
	}
	if (count = 100)
	{
		PixelSearch , px, py, 569, 744, 628, 891 ,0x226699,20,RGB
		if (ErrorLevel=0)
		{
			good := 0
			x = 0
		}
		else
		{
			PixelSearch , px, py, 595, 856, 628, 891 ,0x77b255,20,RGB
			if (ErrorLevel=0)
				good := 0
			else {
				count = 0
				x=-2
			}
		}
	}
}
if (x == 100)
	sleep 1000
Send {Alt down}{tab}
Send {Alt up}
x+= 1
sleep 250
}

y:: 
MouseGetPos, xpos, ypos
send %xpos%
send, {Enter}
send %ypos%
send, {Enter}

Esc::ExitApp
