int main(void){
volatile int *LEDs=(int*)0xFF200000;
volatile int *SW_switch=(int*)0xFF200040;

	while(1)
	{
	int value;	
	value = *SW_switch;
	*LEDs = value;
	}
}