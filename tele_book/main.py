import UI
import book_create as bk
import processing as pr

nb = UI.get_rows()
bk.create_book(nb)

looking_for = UI.get_search()
pr.search_option(looking_for)


