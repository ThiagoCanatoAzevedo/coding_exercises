function stairCase(n) {
    for (let i = 1; i <= n; i++) {

        let spaces = " ".repeat(n - i);
        let hashes = "#".repeat(i);

        console.log(spaces + hashes);
    }
}

stairCase(6);

/*
Exercise anotations:
- Name: Staircase
- Difficulty: Easy
- Score: 10/10
*/