from bazarApp.data.item import dummy_item
from bazarApp.data.item_repo import FileItemRepo


def test_insert_into_file_and_cache():
    filename = "test.test"
    repo = FileItemRepo(filename)
    item = dummy_item()
    repo.upsert(item)
    # update on same repo
    _verify_item_loaded(item, repo)
    # reload repo
    _verify_on_new_repo(item, filename=filename)


def _verify_on_new_repo(item, filename):
    repo = FileItemRepo("test.test")
    _verify_item_loaded(item, repo)


def _verify_item_loaded(item, repo):
    load_item = repo.get(item.id)
    assert item.id == load_item.id
    assert item.name == load_item.name
    assert item == load_item


def test_some_change_is_done():
    filename = "test.test"
    repo = FileItemRepo(filename)
    item = dummy_item()
    repo.upsert(item)
    # update on same repo
    _verify_item_loaded(item, repo)
    # update item and update in repo
    item.name = 'new name of item'
    repo.upsert(item)
    _verify_item_loaded(item, repo)
    # reload repo
    _verify_on_new_repo(item, filename=filename)
