from database.DB_connect import DBConnect
from model.classificazione import Classificazione
from model.gene import Gene
from model.interazione import Interazione


class DAO:
    @staticmethod
    def getGene():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """

        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))

        cursor.close()
        conn.close()
        return result

# GET CROMOSOMI => SELECT DISTINCT CROMOSOMA FROM GENE WHERE CROMOSOMA > 0

    @staticmethod
    def getClassificazione():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM classificazione """

        cursor.execute(query)

        for row in cursor:
            result.append(Classificazione(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getInterazione():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)

        query = """ select distinct least(g1.cromosoma, g2.cromosoma) as cromosoma1, 
                                    greatest(g1.cromosoma, g2.cromosoma) as cromosoma2, 
                                    i.id_gene1, 
                                    i.id_gene2, 
                                    i.correlazione
                    from interazione i, gene g1, gene g2
                    where i.id_gene1 = g1.id  and i.id_gene2 = g2.id and i.correlazione <> 0 
                    group by cromosoma1, cromosoma2 """

        cursor.execute(query)

        for row in cursor:
            result.append(Interazione(**row))

        cursor.close()
        conn.close()
        return result


if __name__ == '__main__':
    dao = DAO()

    interazioni = dao.getInterazione()
    for interazione in interazioni:
        print(interazione)