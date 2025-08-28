//first come first serve

#include <stdio.h>
int main(){
    int n ,i;
    printf ("enter the number of proccesses");
    scanf ( '%d'&,n);
    int at[n],bt[n],ct[n],wt[n],tat[n];
    //input arrival time and burust time
    for (int i=0; i<n; i++){
        printf ("ententer the arrival time");
        scanf ('%d',&at[i]);
        printf ("ententer the brust time");
        scanf ('%d',&bt[i]);

    }
    //sort process by arrival time
    for (i=0; i< n-1; i++){
        for (int j=i+1; j< n; j++){
            if  (at[i]>at[j]){
                //swape arrival time
                int temp = at[i];
                at[i]=at[j];
                at[j]=temp;

                //swape brust time
                temp= bt[i];
                bt[i]=bt[j];
                bt[j]=temp;
                
            }
        }
    }

    int time = 0;
    for(i=0;i<n;i++){
        if (time<at[i]){
            time= at[i];
            ct[i]=time+bt[i];
            tat[i]=ct[i]-at[i];
            wt[i]=tat[i]-bt[i];
            time=ct[i];
        }
    }
    printf ("%d/t%d/t%d/t%d/4%d/n",i+1,at[i],bt[if] ,ct[i] ,tat[if] ,wt[if] ) ;
    return 0; 

}