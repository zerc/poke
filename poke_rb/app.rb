# frozen_string_literal: true

require 'sinatra'
require 'sinatra/reloader' if development?
require 'sinatra/json'

require './requestor'

get '/pokemon/:name' do |name|
  json(get_pokemon(name))
end

get '/pokemon/translated/:name' do |name|
  pokemon = get_pokemon(name)
  description = pokemon[:description]

  pokemon[:description] = if pokemon[:habitat] == 'cave' || pokemon[:isLegendary]
                            as_yoda(description)
                          else
                            as_shakespeare(description)
                          end

  json(pokemon)
end

def get_pokemon(name)
  base = ENV['POKEAPI_BASE_URL'] || 'https://pokeapi.co/api/v2'
  data = request_get("#{base}/pokemon-species/#{name}/")
  description = data['flavor_text_entries'][0] ? data['flavor_text_entries'][0]['flavor_text'] : ''

  {
    name: data['name'],
    description: description,
    habitat: data['habitat'] ? data['habitat']['name'] : '',
    isLegendary: data['is_legendary']
  }
end

def as_yoda(text)
  base = ENV['FUNTRANS_BASE_URL'] || 'https://api.funtranslations.com/translate'
  data = request_post("#{base}/yoda.json", { "text": text })
  data['contents']['translated']
end

def as_shakespeare(text)
  base = ENV['FUNTRANS_BASE_URL'] || 'https://api.funtranslations.com/translate'
  data = request_post("#{base}/shakespeare.json", { "text": text })
  data['contents']['translated']
end
