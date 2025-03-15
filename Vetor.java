package Vetor;

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

    public void adicionarTodos_i(int... elementosi){
        for (int elementoi : elementosi) {
            adicionar(elementoi);
            } 
        }

    public void adicionarTodos__str(String... elementosstr){
        for (int elementostr : elementosstr) {
            adicionar(elementostr);
            } 
        }

    public void adicionarTodos_f(float... elementosf){
        for (int elementof : elementosf) {
            adicionar(elementof);
            } 
        }
    }

    public static void main(String[] args) {
        
    }
    
    }
    

