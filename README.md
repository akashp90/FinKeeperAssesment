# How to run the code?
1. CLone the repository
2. Run `pipenv install`
3. Run `pipenv shell`
4. Run `cd tagsbackend`
5. Run `python manage.py makemigrations tags`
6. Run `python manage.py migrate`
7. Run `python manage.py runserver`
8. Add new posts, add new tags
9. Search for posts with tags

## Search explanation
1. All tags: Includes posts which have all the tags which are specified, and none of the tags specified in the exclude list
2. Any tags: Includes posts which have at least one of the tags specified, and none of the tags specified in the exclude list


## Notes:
1. Due to limited time, I could not fully optimize the system.
2. The query to filter 'all tags' is inefficient, since I am doing the filtering in the application layer, and not at the database layer.
   We can use a generated field as a cache to improve the performance of this query. (i.e, the generated field, say tag_names, should contain
   the comma seperated list of tag names for the post, and this should be updated appropriately.
