# Caching in Django: Property Listings

## Overview

This project demonstrates **Django caching with Redis** and **Dockerized PostgreSQL** for a property listing app.

### ✅ Task 0: Project Setup

* Create Django project and `properties` app.
* Configure **PostgreSQL** as the database and **Redis** as the cache backend.
* Dockerize PostgreSQL and Redis services with `docker-compose`.

### ✅ Task 1: Cache Property List View

* Implement `/properties/` view.
* Apply **@cache_page** decorator to cache response for **15 minutes** in Redis.

### ✅ Task 2: Low-Level Caching

* Use Django **low-level cache API** to store all properties queryset for **1 hour** in Redis.

### ✅ Task 3: Cache Invalidation

* Use **Django signals** to clear cached queryset when properties are created, updated, or deleted.

### ✅ Task 4: Cache Metrics

* Implement `/cache-metrics/` to display Redis **hit/miss stats** and **cache hit ratio**.

---

## 🚀 How to Run

1. **Start containers:**

```bash
docker-compose up --build
```

2. **Run migrations:**

```bash
docker-compose exec web python manage.py migrate
```

3. **Access the app:**

* Property list (cached): **`http://127.0.0.1:8000/properties/`**
* Cache metrics: **`http://127.0.0.1:8000/cache-metrics/`**

---