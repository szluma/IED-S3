package ArrayList;

import java.util.ArrayList;
import java.util.Scanner;

public class listaMenu {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        ArrayList<String> lista = new ArrayList<>();

        int opcao; 
        do {
            System.out.println("\n======= MENU =======");
            System.out.println("1 - Adicionar");
            System.out.println("2 - Remover");
            System.out.println("3 - Exibir");
            System.out.println("0 - Sair");
            System.out.println("Escola uma opção: ");
            opcao = entrada.nextInt();
            entrada.nextLine();

            switch (opcao) {
                case 1:
                System.out.print("Digite algum elemento para ser adicionado");
                String elemento = entrada.nextLine();
                lista.add(elemento);
                    System.out.println("Sucesso");
                    break;

                case 2:
                if (lista.isEmpty()) {
                    System.out.println("Vazio");
                    
                } else {
                    System.out.println("Digite algum elemento para ser removido");
                    int indice = entrada.nextInt();
                    
                    if(indice >= 0 && indice < lista.size()){
                        lista.remove(indice);
                        System.out.println("Sucesso");
                    } else {
                        System.out.println("Este índice é inválido!");
                    }
                }
                break;

                case 3:
                if (lista.isEmpty()) {
                    System.out.println("Vazio");
                } else {
                    System.out.println("Elemento: " + lista);
                }
                break;
                case 0:
                System.out.println("Saindo do programa...");
                break;
                default:
                System.out.println("Opção inválida! Tente novamente");
            }

        } while (opcao != 0);
            entrada.close();
    }
}