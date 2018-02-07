/* TweetStats
 *
 * Fichier       ./front/classes/search.js
 * Description   Classe principale pour effectuer une recherche dans les tweets ainsi que la fonction de recherche
 * Auteurs       Théophile Walter
 */

 class Search {

    /*
     * Constructeur de la classe Search
     * 
     * @params
     *   string: la chaîne de caractères correspondant aux termes à rechercher dans la base
     *   parent: l'élement DOM dans lequel ajouter le résultat HTML de la requête
     * 
     * @notes
     *   La requête peut être longue à s'effectuer, le résultat est affiché à la réponse
     */
    constructor(string, parent) {

        // Définition des attributs
        this.string      = string;
        this.parent      = parent;
        this.element     = null; // L'élement DOM dans lequel mettre le rapport
        this.words       = string.split(/[\s,./;:!?]/g);
        this.url         = "/api/search/" + string;
        this.responseUrl = "/api/get-response/";
        this.requestId   = null; // L'identifiant de la requête (pour attendre la réponse)
        this.interval    = null; // L'intervalle d'attente (setInterval)

        // Crée le conteneur
        this.element = document.createElement("div");
        this.element.className = "search-result";     
        this.element.innerHTML = "Récupération des résultats en cours....";   

        // Ajoute le conteneur au parent
        this.parent.appendChild(this.element);
    }

 }

/*
 * Effectue une recherche dans les tweets
 * 
 * @params
 * 
 * @notes
 *   Récupère les informations dans la page HTML
 */
function searchTweet() {
    var searchInput = document.getElementById('search-input');
    var resultsFeed = document.getElementById('results-feed');
    new Search(searchInput.value, resultsFeed);
    searchInput.value = '';
}