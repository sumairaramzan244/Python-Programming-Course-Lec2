# Python-Programming-Course-Lec2

# Lecture 2 — Variables in Python

---

## 1. Variable kya hoti hai?

Variable ek container hota hai jo data store karta hai. Hum variable ko ek naam dete hain aur baad mein us naam se value access karte hain.

```python
pakistan = 1947
india = "15 August"
print(pakistan)   # Output: 1947
print(india)      # Output: 15 August
```

---

## 2. Print Statement mein Variable Use Karna

### Comma ( , ) se print karna
Python automatically space add karta hai:
```python
print("Pakistan was created in the year", pakistan)
# Output: Pakistan was created in the year 1947
```

### Plus ( + ) operator se print karna
Number variable ko pehle str() se convert karna zaroori hai:
```python
print("Pakistan was established in the year " + str(pakistan))
# Output: Pakistan was established in the year 1947
```
Single aur double quotes dono kaam karte hain — bas properly band hone chahiye.

---

## 3. Variable Overwriting

Same variable naam se dobara value assign karo toh purani value replace ho jati hai:
```python
Ali = 109
Ali = "Ali is a good student"
print(Ali)   # Output: Ali is a good student  (109 nahi)
```

---

## 4. Casting (Data Type Change Karna)

| Function | Kaam | Misaal |
|----------|------|--------|
| `int()` | Integer banata hai | `int(2447)` → `2447` |
| `str()` | String banata hai | `str(1947)` → `"1947"` |
| `float()` | Decimal banata hai | `float(24.0)` → `24.0` |

```python
year  = int(2447)
month = str("June")
day   = float(24.0)
print(year, month, day)   # Output: 2447 June 24.0
```

---

## 5. type() Function — Data Type Check Karna

Kisi bhi variable ka data type pata karne ke liye:
```python
print(type(pakistan))   # <class 'int'>
print(type(india))      # <class 'str'>
```

Common types:
- `int` — poora number jaise 1947
- `str` — text jaise "Pakistan"
- `float` — decimal jaise 24.0

---

## 6. Case Sensitivity

Python case-sensitive language hai — uppercase aur lowercase alag variables hote hain:
```python
pakistan = 1947
Pakistan = "Islamic Republic of Pakistan"
print(pakistan)   # 1947
print(Pakistan)   # Islamic Republic of Pakistan
```
Sirf capital `P` ki wajah se dono bilkul alag variables hain.

---

## 7. Summary

| Concept | Key Point |
|---------|-----------|
| Variable | Data store karne ka container |
| Print with `,` | Automatically space add hoti hai |
| Print with `+` | Number ko `str()` se convert karna zaroori hai |
| Overwriting | Nayi value assign hone se purani replace ho jati hai |
| Casting | `int()`, `str()`, `float()` se data type change hota hai |
| `type()` | Variable ka data type check karta hai |
| Case Sensitive | `pakistan` aur `Pakistan` do alag variables hain |

---

*End of Lecture 2 Notes*
