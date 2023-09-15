const balanceEq = require("chem-eb");
const bodyParser = require("body-parser");

function BalanceEquation(app) {
    app.use(bodyParser.json());
    app.use(bodyParser.urlencoded({ extended: true }));

    // Create a route to receive data and insert it into the database
    app.post("/balance-equation", async (req, res) => {
        const { question } = req.body;
        let userInput = question;

        const result = balanceEq(userInput).outChem;
        res.send(result);
    });
}

module.exports = BalanceEquation;
