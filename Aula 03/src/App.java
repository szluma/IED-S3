import vetor.PrimeiroVetor;

public class App {
    public static void main(String[] args) throws Exception {
       PrimeiroVetor vetor = new PrimeiroVetor(5);

       //valores do vetor
       int [] valores = {10, 20, 30, 40, 50};
       for (int valor : valores) {
        vetor.adicionarTodos(valor);
      }

      //vetor.exibir();
      System.out.println("Indice 2 = " + vetor.getElemento(2));
      System.out.println("quantidade = " + vetor.getTamanho());
      System.out.println("-----------------------------------");
      vetor.removerPorIndice(2);
      vetor.exibir();System.out.println("tamanho do vetor = "+ vetor.getTamanho());
      vetor.exibir();
    }
}
