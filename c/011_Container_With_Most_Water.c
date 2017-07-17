/*
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

Subscribe to see which companies asked this question
*/

/*
在 j 的右端没有一条线会比它高！ 假设存在 k |( j<k && ak > aj) ，那么  由 ak> aj，所以 min( ai,aj, ak) =min(ai,aj) ，所以由i, k构成的容器的容积C' = min(ai,aj ) * ( k-i) > C，与C是最值矛盾，所以得证j的后边不会有比它还高的线；
如果我们目前得到的候选： 设为 x, y两条线（x< y)，那么能够得到比它更大容积的新的两条边必然在  [x,y]区间内并且 ax' > =ax , ay'>= ay;
*/


//define a macro would decrease the time taken;
//first time, mis-tpye the min as max in the function

#define MyMin(x, y) (x>y?y:x)

int maxArea(int* height, int heightSize) {
    
	int i, j;
	int nowMax = 0;
	int c_temp;
	int height_i;
	int height_j;

	if(heightSize <= 1)
		return 0;


	for(i = 0, j = heightSize - 1; i < j;)
	{
	    height_i = *(height+i);
	    height_j = *(height+j);
		c_temp = MyMin( height_i, height_j) * (j - i);
		nowMax = c_temp > nowMax ? c_temp: nowMax;

		if(MyMin(height_i, height_j) == height_i) 	//i is the min height
			i++;
		else
			j--;
	}

	return nowMax;

}