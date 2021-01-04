## Quick Django ORM cheat sheet
**Full: https://github.com/chrisdl/Django-QuerySet-Cheatsheet**

All these functions returns new QuerySets

### 1. Methods that return new QuerySets

**Example:**
```python
Entry.objects.filter(**kwargs).exclude(**kwargs).order_by(**kwargs)
```

* filter
* exclude
* ...

### 2. Operators that return new QuerySets

* AND (&)
* OR (|)

### 3. Methods that do not return QuerySets

* get
* create
* ...

### 4. Field lookups
**Field lookups are how you specify the meat of an 
SQL WHERE clause. They’re specified as keyword arguments 
to the QuerySet methods filter(), exclude() and get().**

**Example:**
```python
Entry.objects.get(id__exact=14)  # note double underscore.
```

* exact
* iexact
* contains
* icontains
* in
* gt
* gte
* lt
* lte
* startswith
* ...

**Protip: Use in to avoid chaining filter() and exclude()**
```python
Entry.objects.filter(status__in=['Hung over', 'Sober', 'Drunk'])
```

