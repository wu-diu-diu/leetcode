
int fac(int n){
    if(n < 0){
        return -1;
    }
    else if (n == 0){
        return 1;
    }
    else{
        return n * fac(n - 1);
    }
}