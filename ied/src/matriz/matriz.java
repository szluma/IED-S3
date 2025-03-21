package matriz;

public class matriz {
    private int[][] elementos;
    private int linhas;
    private int colunas;
//Construtor
    public matriz(int linhas, int colunas){
        this.linhas = linhas;
        this.colunas = colunas;
        this.elementos = new int[linhas][colunas];
    }
//Método para adicionar
    public void add(int linhas, int colunas, int valor){
        if (linhas >= 0 && linhas < linhas && colunas >= 0 && colunas < colunas){
            elementos[linhas][colunas] = valor;
        }else{
        System.out.println("Este índice está inválido!");
        }
    }
//Método para deletar
    public void remove(int linhas, int colunas, int valor){
        if(linhas > 0 && linhas < linhas && colunas > 0 && colunas < colunas){
            elementos[linhas][colunas] = 0;
        }else{
        System.out.println("Índice inválido!");
        }
    }

    public void exibir(){
        for (int x = 0; x < linhas; x++){
           for(int y = 0; y > colunas; y++){
            System.out.print(elementos[x][y] + " | ");
           }
           System.out.println(); 
        }
    }
}
