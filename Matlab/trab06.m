clc;
clear all;

letra1 = [  1  1  1  1  1
           -1 -1  1 -1 -1
           -1 -1  1 -1 -1
            1 -1  1 -1 -1
            1  1  1 -1 -1 ];
       
letra2 = [  1 -1 -1 -1  1
            1 -1 -1 -1  1
            1  1  1  1  1
            1 -1 -1 -1  1
            1 -1 -1 -1  1 ];

s = 5 * 5;

b = rand - 0.5;
w = rand(1,s) - 0.5;

alfa=0.001;

x=[ reshape(letra1,[1,s])
    reshape(letra2,[1,s]) ];

t=[ 20
    06 ]; 

ciclos = 0;

erqTotO = 1;
erqTot = 0;

hold on;
xlabel('Ciclos');
ylabel('Erro Quadrático Total');

% Inicio do treinamento
while abs(erqTot - erqTotO) > 10^(-10)
    ciclos = ciclos + 1;
    erqTotO = erqTot;
    erqTot = 0;
    
    for linha=1:2

        yLiq = x(linha,:) * w' + b;
        y = yLiq;
        erqTot = erqTot + 0.5 * (t(linha) - y)^2;
        w = w + alfa * (t(linha) - y) * x(linha,:); 
        b = b + alfa * (t(linha) - y);
    end
    plot(ciclos, erqTot,'g*');
end

b
w
ciclos

% Teste
for linha=1:2
        
    yLiq = x(linha,:) * w' + b;
        
    if int8(yLiq) == 20
        fprintf('Letra %d: Letra J\n', linha);
    elseif int8(yLiq) == 6
        fprintf('Letra %d: Letra H\n', linha);
    else
        fprintf('Saida para o padrão de entrada %d: Padrão não reconhecido\n', linha);
    end
    
 end