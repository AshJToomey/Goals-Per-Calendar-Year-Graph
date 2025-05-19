# 📈 Goals Per Calendar Year Graph

This is a simple Python script that visualizes how many goals were scored each calendar year. It uses `matplotlib` to plot a line graph based on user input and is perfect for learning basic data visualization techniques in Python.

## 🏗️ Features

* User-friendly command-line input for years and corresponding goal data
* Dynamic line graph with data points and annotations
* Grid layout for easier readability
* Input validation to ensure consistent data
* Clear labeling and formatting
* Optional save-to-file functionality (commented out for now)

## 🗈️ Example

If you input:

```
Enter calendar years (e.g. 2018,2019,2020): 2019,2020,2021,2022  
Enter goals scored in each year (same order): 10,15,8,12
```

You’ll get a line graph like this:

* X-axis: Years (2019 to 2022)
* Y-axis: Goals scored (10, 15, 8, 12)
* Each point annotated with its value

## 🚀 How to Run

1. Make sure you have Python installed.
2. Install matplotlib if needed:

   ```bash
   pip install matplotlib
   ```
3. Run the script:

   ```bash
   python goals_graph.py
   ```

## 💾 Optional Enhancement

If you want to save the graph as an image:
Uncomment this line before `plt.show()` in the code:

```python
plt.savefig("goals_per_year.png")
```

## 🧠 Skills Practiced

* Command-line input handling
* Input validation
* Data visualization with matplotlib
* Labeling and formatting plots
* Annotating data points

## 📂 Project Structure

```
goals_graph.py
README.md
```

## 📝 License

This project is open-source and free to use. Feel free to improve it or adapt it into something bigger!

---

Happy coding!
