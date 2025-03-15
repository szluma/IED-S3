public class Vetor {
    private int[] elementosi;
    private String [] elementosstr;
    private float [] elementosf;
    private int tamanho;

    public Vetor (int capacidade){
        this.elementosi = new int [capacidade];
        this.elementosstr = new String[capacidade];
        this.elementosf = new float[capacidade];
        this.tamanho = 0;
    }

    public void adicionari(int elementoi){
        if (tamanho < elementosi.length){
            elementosi[tamanho] = elementoi;
            tamanho++;
        }else{
            System.out.println("Vetor está cheio");
        }
    }

    public void adicionars(String elementostr){
         if (tamanho < elementosstr.length){
            elementosstr[tamanho] = elementostr;
            tamanho++;
        }else{
            System.out.println("Vetor está cheio");
            }
    }

    public void adicionarf(float elementof){
        if (tamanho < elementosf.length){
            elementosf[tamanho] = elementof;
            tamanho++;
        }else{
            System.out.println("Vetor está cheio");
        }
    }

    public void removerPorIndiceInt(int indice){
        if(indice < 0 || indice >= tamanho){
            System.out.println("Índice inválido!");
            return;
        }
    
        for(int i = indice; i < tamanho - 1; i++){
            elementosi[i] = elementosi[i+1];
        }
        tamanho--;
        }

    public void removerPorIndiceStr(int indice){
        if(indice < 0 || indice >= tamanho){
            System.out.println("Índice inválido!");
            return;
        }
    
        for(int i = indice; i < tamanho - 1; i++){
                elementosstr[i] = elementosstr[i+1];
        }
        tamanho--;
        }

    public void removerPorIndiceFloat(int indice){
        if(indice < 0 || indice >= tamanho){
            System.out.println("Índice inválido!");
            return;
        }
    
        for(int i = indice; i < tamanho - 1; i++){
            elementosf[i] = elementosf[i+1];
        }
            tamanho--;
        }
    
    public void removerPorIndiceNuloInt(int indice){
        if(indice >=0 && indice < tamanho){
            System.out.println("Este índice está inválido!");
            return;
        }
        elementosi[indice] =  (Integer) null;
    }

    public void removerPorIndiceNuloF(int indice){
        if(indice >=0 && indice < tamanho){
            System.out.println("Este índice está inválido!");
            return;
        }
        elementosf[indice] = (Float) null;
    }

    public void removerPorIndiceNuloStr(int indice){
        if(indice >=0 && indice < tamanho){
            System.out.println("Este índice está inválido!");
            return;
        }
        elementosstr[indice] = null;
    }

    public void exibirInt(){

        System.out.println("Vetor ");
        for (int i = 0; i < tamanho; i++) {
            System.out.println(elementosi[i] + " ");
            
            }
    
        }

    public void exibirStr(){

    System.out.println("Vetor ");
    for (int i = 0; i < tamanho; i++) {
        System.out.println(elementosstr[i] + " ");
            
            }
    
        }
    
    public void exibirF(){

        System.out.println("Vetor ");
        for (int i = 0; i < tamanho; i++) {
            System.out.println(elementosf[i] + " ");
                    
            }
            
        }

    public int  getElementoInt(int indice){
        if (indice >=0 && indice < tamanho){
            return elementosi[indice];
        }
        throw new IndexOutOfBoundsException("índice inválido" + indice);
    }
    
    public int getTamanho() {
        return tamanho;
    }

    public float getElementofloat(int indice){
        if (indice >=0 && indice < tamanho){
            return elementosf[indice];
        }
        throw new IndexOutOfBoundsException("índice inválido" + indice);
    }

    public String getElemento(int indice){
        if (indice >=0 && indice < tamanho){
            return elementosstr[indice];
        }
        throw new IndexOutOfBoundsException("índice inválido" + indice);
    }
    
    public static void main(String[] args) {
        Vetor Tatu = new Vetor(3);
        Tatu.adicionarf(2.1f);
        Tatu.exibirF();System.out.println("Tamanho deste vetor é float = " + Tatu.getTamanho()); 

        Vetor Lobo = new Vetor(3);
        Lobo.adicionari(6);
        Lobo.exibirInt();Lobo.exibirF();System.out.println("Tamanho deste vetor é inteiro = " + Lobo.getTamanho());


        Vetor Cachorro = new Vetor(3);
        Cachorro.adicionars("jaguatirica");
        Cachorro.exibirStr();Cachorro.exibirF();System.out.println("Tamanho deste vetor é String = " + Cachorro.getTamanho());

        
    }
}

    
