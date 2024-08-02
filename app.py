from flask import Flask, request, jsonify

app = Flask(__name__)

def calculer_mensualite(montant_emprunte, taux_annuel, duree_annees):
    taux_mensuel = taux_annuel / 12 / 100
    nombre_mensualites = duree_annees * 12
    mensualite = montant_emprunte * taux_mensuel / (1 - (1 + taux_mensuel) ** -nombre_mensualites)
    cout_total = mensualite * nombre_mensualites - montant_emprunte
    return mensualite, cout_total

@app.route('/calculer', methods=['POST'])
def calculer():
    data = request.json
    montant_emprunte = data['montant_emprunte']
    taux_annuel = data['taux_annuel']
    duree_annees = data['duree_annees']
    mensualite, cout_total = calculer_mensualite(montant_emprunte, taux_annuel, duree_annees)
    return jsonify({
        'mensualite': mensualite,
        'cout_total': cout_total
    })

if __name__ == '__main__':
    app.run(debug=True)
