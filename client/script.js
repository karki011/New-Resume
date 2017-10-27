function prime(n) {
    var num = 2;
    while (n > num ) {
        if (n % num === 0) {
            return false;
            
        }else{
            num++;
        }
        return true;
    }
}