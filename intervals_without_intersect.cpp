#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
struct interval
{int x;
int y;
}; 
bool cmp(interval a,interval b)
{
	if (a.y!=b.y) return a.y<b.y;
	else return a.x<b.x;
};
int main()
{
	int N,result=1,recordy;
	scanf("%d",&N);
	interval a[N];
	for (int i=0;i<N;i++)
		scanf("%d %d",&a[i].x,&a[i].y);
	sort(a,a+N,cmp);
	recordy=a[0].y;
	for (int i=1;i<N;i++)
	{
	
		if (recordy<=a[i].x)
		{
		
			result++;
			recordy=a[i].y;
		}

	}
	printf("%d",result);
	return 0;
}
