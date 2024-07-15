# How to run the code?
1. CLone the repository
2. Run `pipenv shell`
3. Run `cd tagsbackend`
4. Run `python manage.py makemigrations tags`
5. Run `python manage.py migrate`
6. Run `python manage.py runserver`
7. Add new posts, add new tags
8. Search for posts with tags


## Notes:
1. Due to limited time, I could not fully optimize the system.
2. The query to filter 'all tags' is inefficient, since I am doing the filtering in the application layer, and not at the database layer.
   We can use a generated field as a cache to improve the performance of this query. (i.e, the generated field, say tag_names, should contain
   the comma seperated list of tag names for the post, and this should be updated appropriately.
