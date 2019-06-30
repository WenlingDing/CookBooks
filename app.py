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
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country  ORDER BY recipe.date DESC")
    user = cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_user=user,all_countries=countries,all_cuisine=cuisine)

# all recipes ordered by recipe name
@app.route('/sort1')
def orderByRecipe():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country ORDER BY recipe.name")
    user = cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_user=user,all_countries=countries,all_cuisine=cuisine)
    
# all recipes ordered by author name
@app.route('/sort2')
def orderByAuthor():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country ORDER BY user.name")
    user = cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_user=user,all_countries=countries,all_cuisine=cuisine)
    
# all recipes ordered by cuisine
@app.route('/sort3')
def orderByCuisine():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country ORDER BY recipe.cuisine_id")
    user = cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_user=user,all_countries=countries,all_cuisine=cuisine)

#all recipes listed by date ASC
@app.route('/sort4')
def orderByDate():
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country ORDER BY recipe.date")
    user = cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_user=user,all_countries=countries,all_cuisine=cuisine)
 
#choose recipes in different country
@app.route('/country/<id>')
def country(id):
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country where country.id = " + id)
    user=cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    return render_template('home.html', all_countries=countries, all_user=user, all_cuisine=cuisine)

#choose recipes in different cuisine
@app.route('/cuisine/<id>')
def cuisine(id):
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country where cuisine.id = " + id)
    user=cursor.fetchall()
    cursor.execute("SELECT * From cuisine")
    cuisine=cursor.fetchall()
    cursor.execute("SELECT * From country")
    countries=cursor.fetchall()
    return render_template('home.html', all_cuisine=cuisine,all_user=user,all_countries=countries)
    
#the recipe details page, one recipe one single page
@app.route('/recipe/<recipe_id>', methods=['GET'])
def see_more(recipe_id):
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute("SELECT recipe.intro AS intro, user.id, user.name AS user_name, country.name AS country, recipe.date AS date, recipe.name AS recipe_name, cuisine.name AS cuisine_name, recipe.ingredients AS ingredients FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country WHERE recipe.id = " + recipe_id)
    recipe=cursor.fetchall()
    cursor.execute("SELECT  `description` FROM recipe_process WHERE recipe_process.recipe = %s ORDER BY `step`",recipe_id)
    process = cursor.fetchall()
    print(process)
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
        user = request.form['user_name']
        country_id = request.form['country']
        name = request.form['recipe_name']
        cuisine_id = request.form['cuisine']
        intro =request.form['intro']
        ingredients = request.form['ingredients']
        sql1 = """INSERT INTO `user` (`name`, `country`) VALUES ("{}", {})""".format(user, country_id)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql1)
        conn.commit()
        sql2 = """INSERT INTO `recipe` (`user`, `name`, `ingredients`, `cuisine_id`, `intro`) VALUES (last_insert_id(), "{}" ,"{}", {}, "{}") """.format(name, ingredients, cuisine_id, intro)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql2)
        conn.commit()
        recipe_id=cursor.lastrowid
        description = request.form.getlist('description')
        recipeProcess=(recipe_id,description)
        counter = 1
        cursor = pymysql.cursors.DictCursor(conn)
        for i in recipeProcess[1]:
             sql3 ="""INSERT INTO `recipe_process` ( `recipe`, `step` ,`description`) 
                VALUES (%s, %s, %s);"""
             sql3_input = (recipeProcess[0],counter,i)
             cursor.execute(sql3,sql3_input)    
             counter+=1
        conn.commit()
        cursor.close()
        return redirect('/') 
                
@app.route('/edit/<recipe_id>', methods=['GET', 'POST'])
def edit(recipe_id):
    if request.method == 'GET':
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute("SELECT * from recipe WHERE recipe.id = " + recipe_id)
        recipe=cursor.fetchone()
        cursor.execute("SELECT  `description` FROM recipe_process WHERE recipe_process.recipe = " + recipe_id)
        process = cursor.fetchall()
        cursor.execute("SELECT * FROM cuisine")
        cuisine=cursor.fetchall()
        return render_template('edit.html', recipe=recipe, all_process=process, all_cuisine=cuisine)
    else:
        name = request.form['recipeName']
        intro = request.form['intro']
        cuisine_id = request.form['cuisine']
        ingredients = request.form['ingredients']
        sql1 = """
            UPDATE recipe SET name = "{}", intro = "{}", ingredients = "{}" WHERE recipe.id = {} """.format(name, intro, ingredients, recipe_id)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql1)
        conn.commit()
        # delete all process then update all so that it is can update new row 
        sql2 = "DELETE FROM recipe_process WHERE recipe_process.recipe =" + recipe_id.format(recipe_id)
        cursor = pymysql.cursors.DictCursor(conn)
        cursor.execute(sql2)
       
        description = request.form.getlist('description')
        recipeProcess=(recipe_id,description)
        counter = 1
        cursor = pymysql.cursors.DictCursor(conn)
        for i in recipeProcess[1]:
             sql3 ="""INSERT INTO `recipe_process` ( `recipe`, `step` ,`description`) 
                VALUES (%s, %s, %s);"""
             sql3_input = (recipeProcess[0],counter,i)
             cursor.execute(sql3,sql3_input)    
             counter+=1
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
        sql = """SELECT recipe.date AS date, recipe.intro AS intro, recipe.id AS recipe_id, user.name AS user_name, country.name AS country, recipe.name AS recipe_name, cuisine.name AS cuisine_name FROM user INNER JOIN recipe ON user.id = recipe.user INNER JOIN cuisine ON cuisine.id = recipe.cuisine_id INNER JOIN country ON country.id = user.country WHERE recipe.name LIKE '%""" + search_for + "%'"
    cursor = pymysql.cursors.DictCursor(conn)
    cursor.execute(sql)
    search = cursor.fetchall()
    return render_template('search.html', all_search=search)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)