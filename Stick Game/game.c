/*
In this stick game, we can pick 1 or 2 or 3 stick and whoever pick last stick, loss the game.

*/


//stick game
#include <stdio.h>
int main()
{
    int n,m,x,y;
    printf("Enter number of sticks : ");
    scanf("%d",&n);
    printf("Enter 1 if you want to start \n");
    printf("Enter 2 if you want computer to start \n");
    scanf("%d",&y);
//    if((n%4!=1&&y==2)||(n%4==1&&y==1)){
//    	printf("you have no chance to win   \n");
//    }
//	else{
//		printf("you have chance to win   \n");
//	}
    if(y==1){
	    while(n!=0){
	        printf("Enter the number of sticks(1 or 2 or 3) you want to pick:");
	        scanf("%d",&m);
	        printf("you picked up %d sticks \n",m);
	        n-=m;
	        printf("sticks left %d \n",n);
	        if(n==1){
	            printf("you won the game  \n");
	            break;
	        }
	        x=(n-1)%4;
	        if(x==0){
	        	x=1;
	        	printf("computer picked up %d sticks\n",x);
			}
			else{
	        printf("computer picked up %d sticks\n",x);
	    	}
	        n-=x;
	        printf("sticks left %d \n",n);
	        if(n==1){
	            printf("computer won the game  \n");
	            break;
	        }
    	}
    }
    else{
    	while(n!=0){
	        x=(n-1)%4;
	        if(x==0){
	        	x=1;
	        	printf("computer picked up %d sticks\n",x);
			}
			else{
	        printf("computer picked up %d sticks\n",x);
	    	}
	        n-=x;
	        printf("sticks left %d \n",n);
	        if(n==1){
	            printf("computer won the game  \n");
	            break;
	        }
	        printf("Enter the number of sticks(1 or 2 or 3) you want to pick:");
	        scanf("%d",&m);
	        printf("you picked up %d sticks \n",m);
	        n-=m;
	        printf("sticks left %d \n",n);
	        if(n==1){
	            printf("you won the game  \n");
	            break;
	        }
	    }
	}
    return 0;
}
