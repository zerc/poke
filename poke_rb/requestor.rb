# frozen_string_literal: true

require 'uri'
require 'net/http'
require 'json'

def request_get(url)
  uri = URI(url)
  response = Net::HTTP.get_response(uri)
  JSON.parse(response.body) if response.is_a?(Net::HTTPSuccess)
end
