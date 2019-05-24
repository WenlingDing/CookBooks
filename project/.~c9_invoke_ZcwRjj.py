from flask import Flask
from flask import render_template,request, redirect
import os
import pymysql

app =Flask(__name__)

conn = pymysql.connect(host='remotemysql.com',
                             user ='vnUzDcqd18',
                             password='b1PxZXOQ7V',
                             db='vnUzDcqd18',
                             port=3306)

@app.route('/')
def home():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country")
    user = cursor.fetchall()
    return render_template('home.html', all_user=user)

#the recipe details page
@app.route('/recipe/<recipe_id>', methods=['GET'])
def see_more(recipe_id):
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.intro AS intro, user.id, user.name AS user_name, country.name AS country, recipe.date AS date, recipe.name AS recipe_name, cuisine.name AS cuisine_name, recipe.ingredients AS ingredients FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country WHERE recipe.id = " + recipe_id)
    recipe=cursor.fetchall()
    cursor.execute("SELECT  `description` ,  `step` FROM recipe_process WHERE recipe_process.recipe = " + recipe_id)
    process = cursor.fetchall()
    return render_template('recipe.html', recipe=recipe, all_process=process)
 
 
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute("SELECT * from recipe")
        recipe = cursor.fetchall()
        cursor.execute("SELECT * from recipe_process")
        recipe_process = cursor.fetchall()
        cursor.execute("SELECT * FROM cuisine")
        cuisine = cursor.fetchall()
        cursor.execute("SELECT * FROM country")
        countries = cursor.fetchall()
        return render_template('add.html', all_recipe = recipe, all_cuisine=cuisine, all_countries=countries, recipe_process=recipe_process )
    else:
        print(request.form)
        user = request.form['user_name']
        country_id = request.form['country']
        name = request.form['recipe_name']
        cuisine_id = request.form['cuisine']
        intro =request.form['intro']
        ingredients = request.form['ingredients']
        step = request.form['step']
        description = request.form['description']
        sql = """
            INSERT INTO `user` (`name`, `country`) VALUES ("{}", {});
            SET @last_id_in_user = LAST_INSERT_ID();
            INSERT INTO `recipe` (`user`, `name`, `ingredients`, `cuisine_id`, `intro`) VALUES (@last_id_in_user, "{}" ,"{}", {}, "{}");
            SET @last_id_in_recipe = LAST_INSERT_ID();
            INSERT INTO `recipe_process` (`recipe`, `step` ,`description`)   
            VALUES (@last_id_in_recipe, {}, "{}")
        """.format(user, country_id, name, ingredients, cuisine_id, intro, step, description)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return redirect('/')   
    
@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    if request.method == 'GET':
        cursor = pymysql.cursors .DictCursor(conn)
        cursor.execute("SELECT * from recipe WHERE recipe.id = " + recipe_id)
        recipe=cursor.fetchone()
        cursor.execute("SELECT  `description` ,  `step` FROM recipe_process WHERE recipe_process.recipe = " + recipe_id)
        process = cursor.fetchall()
        cursor.execute("SELECT * FROM cuisine")
        cuisine=cursor.fetchall()
        return render_template('edit.html', recipe=recipe, all_process=process, all_cuisine=cuisine)
    else:
        name = request.form['recipeName']
        intro = request.form['intro']
        cuisine_id = request.form['cuisine']
        ingredients = request.form['ingredients']
        step = request.form['step']
        description = request.form['description']
        sql = """
            UPDATE recipe SET  
                name = "{}",
                intro = "{}",
                cuisine_id = "{}",
                ingredients = "{}",
            WHERE recipe.id =
        """ + recipe_id.format(name, intro, cuisine_id, ingredients)
        sql = """
         UPDATE `recipe_process` SET 
             `step` = "{}",
         WHERE recipe_process.recipe = """ + recipe_id.format(step, description)
         WHERE recipe_process.recipe = """ + recipe_id.format(step, description)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return redirect('/')    
   
@app.route('/delete/<recipe_id>') 
def delete(recipe_id):
    sql = "DELETE FROM recipe WHERE recipe.id =" + recipe_id.format(recipe_id)
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute(sql)
    conn.commit()
    return redirect('/')

# do search  
@app.route('/search')
def search():
    if 'search' not in request.args:
        sql = "SELECT * from recipe"
    else:
        search_for = request.args['search']
        sql = "SELECT * from recipe WHERE name LIKE '%" + search_for + "%'"
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute(sql)
    search = cursor.fetchall()
    return render_template('search.html', all_search=search)
  
  
  
  
  

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)