### Requisitos
* Python 3.10.4 ou maior

### Execução
```bash
git clone git@github.com:marcelinoavelar/bco-imb.git
``` 
```bash
cd bco-imb
``` 
```bash
python -m venv .venv
``` 
```bash
source .venv/bin/activate #Linux
``` 
```bash
pip install -r requirements.txt
``` 
```bash
make test
``` 

Para listar opções da execução do programa executa no terminal:
```bash
python main.py -h 
``` 
Retorno:
```bash
options:
  -h, --help            show this help message and exit

  -s SIMULATIONS, --simulations SIMULATIONS
                        Number of simulations
  -d ROUNDS, --rounds ROUNDS
                        Number of rounds
  -x MIN_PRICE, --min_price MIN_PRICE
                        Minimum value for random property price generation
  -p MAX_PRICE, --max_price MAX_PRICE
                        Maximum value for random property price generation
  -r MIN_RENTAL, --min_rental MIN_RENTAL
                        Minimum value for random generation of rental properties
  -t MAX_RENTAL, --max_rental MAX_RENTAL
                        Maximum value for random generation of rental properties
  -c GAME_PROPERTIES, --game_properties GAME_PROPERTIES
                        Number of properties

``` 


```bash
python main.py --simulations 300 --rounds 1000 --min_price 250_000.00 --max_price 750_000.00 --min_rental 5_000.00 --max_rental 15_000.00 --game_properties 20
``` 

```json
{
  "round_end_per_timeout": 112,
  "average_rounds_per_game": 376.01,
  "winners_percent_by_profile": {
    "PlayerPicky": 28.67,
    "PlayerRandom": 33.0,
    "PlayerInpulsive": 15.0,
    "PlayerCautious": 23.33
  },
  "top winner": "PlayerRandom"
}
```