#include <stdio.h>
void full(int index,int* a,int N,int* hash,int* result)
{
	
	if (index==N)
	{
		for (int i=0;i<N;i++)
		printf("%d",result[i]);
		printf("\n");
	}
	else
	{
		for (int x=0;x<N;x++)
		if (hash[x]==0)
		{
			hash[x]=1;
			result[index]=a[x];
			full(index+1,a,N,hash,result);
			hash[x]=0;
		}
	}
}
int main()
{
	int N;
	printf("please input number N, which means N intergers\n");
	scanf("%d",&N);
	int a[N],hash[N]={0},result[N]={0};
	printf("please input the N intergers\n");
	for (int i=0;i<N;i++)
	scanf("%d",&a[i]);
	int index=0;
	full(index,a,N,hash,result);
	return 0;
}
