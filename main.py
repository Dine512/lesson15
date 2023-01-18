import sqlite3


def get_animal_by_index(index):
    connect = sqlite3.connect('animal2.db')
    cur = connect.cursor()
    query1 = f"""SELECT "index", age_upon_outcome, animal_id, animal_type, name, breed.breed , date_of_birth, outcome.subtype, outcome."type" , outcome."month" , outcome."year"   
                FROM animals_new
                JOIN breed ON animals_new.breed_id  = breed.id
                JOIN outcome ON animals_new."index"  = outcome.id_animal 
                WHERE "index" = {index} 
            """
    query2 = f"""SELECT colors.color  
                FROM animals_new
                JOIN animal_colors ON animal_colors.id_animal = animals_new."index" 
                JOIN colors ON colors.id = animal_colors.id_color
                WHERE "index" = {index}
                """
    result_query = cur.execute(query1).fetchall()
    result_query2 = cur.execute(query2).fetchall()
    result = {"index": result_query[0][0],
              "age_upon_outcome": result_query[0][1],
              "animal_id": result_query[0][2],
              "animal_type": result_query[0][3],
              "name": result_query[0][4],
              "breed": result_query[0][5],
              "date_of_birth": result_query[0][6],
              "colors": ', '.join([item[0] for item in result_query2]),
              "outcome_subtype": result_query[0][7],
              "outcome_type": result_query[0][8],
              "outcome_month": result_query[0][9],
              "outcome_year": result_query[0][10]
    }
    connect.commit()
    cur.close()
    return result
