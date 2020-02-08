# Update ingredient stock

prod1 = """
UPDATE Stock s, Basket b
SET s.pâte = s.pâte-(b.serving*b.quantity), s.sauce_tomates = s.sauce_tomates-(b.serving*b.quantity),
s.mozzarella = s.mozzarella-(b.serving*b.quantity), s.olives = s.olives-(b.serving*b.quantity)
"""

prod2 = """
UPDATE Stock s, Basket b
SET s.pâte = s.pâte-(b.serving*b.quantity), s.sauce_tomates = s.sauce_tomates-(b.serving*b.quantity),
s.mozzarella = s.mozzarella-(b.serving*b.quantity), s.olives = s.olives-(b.serving*b.quantity), s.jambon = s.jambon-(b.serving*b.quantity),
s.champignons = s.champignons-(b.serving*b.quantity)
"""

prod3 = """
UPDATE Stock s, Basket b
SET s.pâte = s.pâte-(b.serving*b.quantity), s.sauce_tomates = s.sauce_tomates-(b.serving*b.quantity),
s.mozzarella = s.mozzarella-(b.serving*b.quantity), s.olives = s.olives-(b.serving*b.quantity), s.câpres = s.câpres-(b.serving*b.quantity),
s.anchois = s.anchois-(b.serving*b.quantity)
"""

prod4 = """
UPDATE Stock s, Basket b
SET s.pâte = s.pâte-(b.serving*b.quantity), s.sauce_tomates = s.sauce_tomates-(b.serving*b.quantity),
s.mozzarella = s.mozzarella-(b.serving*b.quantity), s.olives = s.olives-(b.serving*b.quantity), s.jambon = s.jambon-(b.serving*b.quantity),
s.champignons = s.champignons-(b.serving*b.quantity), s.artichauds = s.artichauds-(b.serving*b.quantity)
"""

prod5 = """
UPDATE Stock s, Basket b
SET s.pâte = s.pâte-(b.serving*b.quantity), s.sauce_tomates = s.sauce_tomates-(b.serving*b.quantity),
s.mozzarella = s.mozzarella-(b.serving*b.quantity), s.olives = s.olives-(b.serving*b.quantity), s.champignons = s.champignons-(b.serving*b.quantity), 
s.artichauds = s.artichauds-(b.serving*b.quantity), s.aubergines = s.aubergines-(b.serving*b.quantity), s.courgettes = s.courgettes-(b.serving*b.quantity)
"""

prod_q = [prod1, prod2, prod3, prod4, prod5]

# Update unit stock

update_prod1 = """
UPDATE UnitStock u
JOIN Stock s ON u.pos = s.pos
SET u.remaining_units = s.pâte
WHERE u.product = 1
"""

update_prod2 = """
UPDATE UnitStock u
JOIN Stock s ON u.pos = s.pos
SET u.remaining_units = (SELECT LEAST(s.jambon, s.champignons) 
WHERE s.pâte >= s.jambon AND s.pâte >= s.champignons)
WHERE u.product = 2
"""

update_prod3 = """
UPDATE UnitStock u
JOIN Stock s ON u.pos = s.pos
SET u.remaining_units = (SELECT LEAST(s.câpres, s.anchois) 
WHERE s.pâte >= s.câpres AND s.pâte >= s.anchois)
WHERE u.product = 3
"""

update_prod4 = """
UPDATE UnitStock u
JOIN Stock s ON u.pos = s.pos
SET u.remaining_units = (SELECT LEAST(s.jambon, s.champignons, s.artichauds) 
WHERE s.pâte >= s.jambon AND s.pâte >= s.champignons AND s.pâte >= s.artichauds)
WHERE u.product = 4
"""

update_prod5 = """
UPDATE UnitStock u
JOIN Stock s ON u.pos = s.pos
SET u.remaining_units = (SELECT LEAST(s.champignons, s.artichauds, s.aubergines, s.courgettes) 
WHERE s.pâte >= s.champignons AND s.pâte >= s.artichauds AND s.pâte >= s.aubergines AND s.pâte >= s.courgettes)
WHERE u.product = 5
"""

update_q = [update_prod1, update_prod2, update_prod3, update_prod4, update_prod5]
