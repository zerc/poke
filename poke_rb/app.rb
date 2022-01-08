# frozen_string_literal: true

require 'sinatra'
require 'sinatra/reloader' if development?
require 'sinatra/json'

require './requestor'

get '/pokemon/:name' do |name|
  json(get_pokemon(name))
end

def get_pokemon(name)
  base = ENV['POKEAPI_BASE_URL'] || 'https://pokeapi.co/api/v2'
  data = request_get("#{base}/pokemon-species/#{name}/")
  description = data['flavor_text_entries'][0] ? data['flavor_text_entries'][0]['flavor_text'] : ''

  {
    name: data['name'],
    description: description,
    habitat: data['habitat'] ? data['habitat']['name'] : '',
    isLegendary: (data['is_legendary'] == 'True')
  }
end
