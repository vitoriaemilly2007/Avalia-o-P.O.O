from base import Fase
from util import JogoUtil

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Você é [seu nome], um usuário comum que encontra, por acidente, um celular abandonado pertencente a [nome da pessoa desaparecida]. O telefone está cheio de mensagens estranhas, fotos e vídeos inquietantes. Conforme você explora o aparelho, a linha entre a realidade e a simulação começa a se desfazer. Você se vê preso em um pesadelo digital onde nada é o que parece. 
        Você encontra o celular abandonado. O que vai fazer?
        '''
        self.__opcoes = ["Tentar desbloquear o celular", "Desistir e chamar a polícia"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return InvestigarCelular()
        else:
            return ChamarPolicia()

class InvestigarCelular(Fase):
    def __init__(self):
        self.__descricao = " Você está dentro de um prédio abandonado, onde acredita que o Fragmento da Mente está escondido. Um som ecoa pelos corredores. Você segue o barulho?"
        self.__opcoes = ["Sim, Você encontra um homem misterioso que oferece informações valiosas, mas em troca quer algo de você. Vá para a próxima decisão.", "Não, Você ignora o som e segue explorando, mas se perde dentro do labirinto do prédio e acaba preso em um loop infinito (Final: O Laço Infinito)."]

    def executar(self):
        print("\nInvestigação")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return ContinuarInvestigacao()
        else:
            return FinalOlacoInfinito()

class ContinuarInvestigacao(Fase):
    def __init__(self):
        self.__descricao = "O homem misterioso pede que você aposte um item no Cassino para conseguir a localização exata do Fragmento. Você aceita?"
        self.__opcoes = ["Sim, Você joga com o Dado Dourado e obtém as coordenadas. Vá para a próxima decisão.", "Não, Sem informações, você vaga sem rumo e descobre tarde demais que estava em uma simulação sem saída (Final: A Simulação Continua)."]

    def executar(self):
        print("\nInvestigação Avançada")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return RealidadeDistorcida()
        else:
            return FinalAsimulaoContinua()

class RealidadeDistorcida(Fase):
    def __init__(self):
        self.__descricao = "Você encontrou o Fragmento da Mente em um cofre trancado. Você tem a Chave Codificada para abri-lo?"
        self.__opcoes = ["Sim, Você desbloqueia o cofre e segura o Fragmento. Vá para a próxima decisão.", "Não, Incapaz de acessar o artefato, você continua preso em um ciclo de tentativas fracassadas, perdendo-se entre realidades (Final: Desconexão Total)."]

    def executar(self):
        print("\nDistorção da Realidade")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return ()
        else:
            return FinalDesconexãoTotal()

class ChamarPolicia(Fase):
    def __init__(self):
        self.__descricao = "Agora que tem o Fragmento, sua mente se enche de lembranças apagadas. Você percebe que foi enganado por Noctis e que sua identidade é uma mentira. Você destrói o Fragmento?"
        self.__opcoes = ["Sim,  O artefato é destruído, mas com ele, todas as suas memórias desaparecem. Você nunca mais saberá quem foi (Final: Memória Roubada).", "Não, Você mantém o Fragmento e segue em busca de mais respostas. Vá para a próxima decisão."]

    def executar(self):
        print("\nChamar a Polícia")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalMemoriaroubada()
        else:
            return ()

class VideoRevelador(Fase):
    def __init__(self):
        self.__descricao = "Você descobre que o Fragmento pode alterar a realidade à sua vontade. Você o utiliza para reescrever seu passado e controlar o mundo ao seu redor??"
        self.__opcoes = ["Sim, Você se torna um ser onipotente, capaz de manipular todas as camadas do sonho e da realidade (Final: Controle Absoluto).", "Não, Você resiste à tentação e decide buscar a verdade real. Vá para a próxima decisão."]

    def executar(self):
        print("\nVídeo Revelador")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalControleAbsoluto()
        else:
            return ()

class ManipulacaoVortice(Fase):
    def __init__(self):
        self.__descricao = "Você está prestes a despertar, mas percebe que algo parece diferente. Está pronto para aceitar essa nova realidade?"
        self.__opcoes = ["Sim, Você desperta no mundo real, mas pequenos detalhes parecem fora do lugar, deixando dúvidas sobre sua percepção (Final: Despertar na Verdade).", "Não, Você hesita, temendo que esta realidade seja apenas mais uma ilusão, e acaba preso para sempre em sua própria mente (Final: Desconexão Total)"]

    def executar(self):
        print("\nManipulação de Vórticee")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return FinalDespertarnaVerdade()
        else:
            return FinalDesconexãoTotal()


class FinalDespertarnaVerdade(Fase):
    def executar(self):
        print("\nFinal: (Fulano) encontra o Fragmento da Mente e descobre que toda a missão era um teste para determinar se ele era digno de conhecer a verdadeira natureza da realidade. Ele desperta no mundo real, mas nada parece exatamente como antes, e ele(a) se sente estranho(a).")
        return None

class FinalOlacoInfinito(Fase):
    def executar(self):
        print("\nFinal: (Fulano) falha em recuperar o Fragmento e percebe que está preso(a) dentro de um loop eterno, revivendo os mesmos eventos sem parar, pra sempre.")
        return None

class FinalAsimulaoContinua(Fase):
    def executar(self):
        print("\nFinal: Mesmo ao recuperar o Fragmento, (fulano) percebe que sua realidade ainda é uma simulação, e que há um nível mais profundo que ele nunca poderá acessar.")
        return None

class FinalMemoriaroubada(Fase):
    def executar(self):
        print("\nFinal: (fulano)descobre que nunca foi um(a) agente, mas sim o verdadeiro criador do Fragmento da Mente. Ele(a) escolhe destruir o artefato, perdendo todas as suas memórias no processo.")
        return None

class FinalControleAbsoluto(Fase):
    def executar(self):
        print("Ao dominar todas as camadas do sonho e reunir todos os itens, (fulano) assume controle total sobre a realidade e passa a manipular o mundo como se fosse um deus, e se torna o verdadeiro vilão/vilã da história.")
        return None

class FinalDesconexãoTotal(Fase):
    def executar(self):
        print("(fulano)falha em distinguir a ilusão da realidade, enlouquecendo e se tornando apenas mais uma projeção no mundo dos sonhos, esquecido(a) para sempre.")
        return None