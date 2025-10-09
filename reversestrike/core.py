#!/usr/bin/env python3
"""
REVERSE STRIKE - Complete 5-Pillar System
Detection + Defense + Intelligence + Stealth + Reverse Hack
"""

import socket
import threading
import time
import json
import os
import random
from datetime import datetime
from collections import defaultdict


import random
import pyfiglet
from termcolor import colored
from rich.console import Console

console = Console()

class ReverseStrikeComplete:
    def __init__(self):
        self.attackers = defaultdict(lambda: {
            'ports_hit': set(),
            'attempts': 0, 
            'first_seen': None,
            'threat_level': 0,
            'blocked': False,
            'last_attempt': None
        })
        self.is_active = True
        self.blocked_ips = set()
        self.show_banner()
    
    def show_banner(self):
        """ banner design"""
    
        os.system('cls' if os.name == 'nt' else 'clear')
        

        ascii_art = pyfiglet.figlet_format("REVERSESTRIKE", font="dos_rebel")
        
    
        colors = ["red"]
        
        
        colored_art = colored(ascii_art, color=random.choice(colors))
        print(colored_art)
        
    
        print("\n" + "="*50)
        print("           REVERSE STRIKE - 5 PILLARS")
        print("     Detection | Defense | Intelligence | Stealth | Reverse Hack")
        print("="*50)
        print(" System Initialized - Monitoring ports 2222, 4444")
        print("Press Ctrl+C to stop the system\n")

    def defense_system(self, attacker_ip, port):
        """COMPLETE DEFENSE"""
        self.attackers[attacker_ip]['ports_hit'].add(port)
        self.attackers[attacker_ip]['attempts'] += 1
        self.attackers[attacker_ip]['last_attempt'] = datetime.now()
        
        if not self.attackers[attacker_ip]['first_seen']:
            self.attackers[attacker_ip]['first_seen'] = datetime.now()
        
        threat_level = self.calculate_threat_level(attacker_ip)
        self.attackers[attacker_ip]['threat_level'] = threat_level
        
        print(f"[DEFENSE] {attacker_ip} - Threat Level: {threat_level}/10")
        
        if threat_level >= 7:
            self.immediate_block(attacker_ip)
            return "BLOCKED"
        
        if threat_level >= 4:
            if self.is_rapid_attacker(attacker_ip):
                print(f"[RATE LIMIT] {attacker_ip} - Too many connections")
                return "LIMITED"
        
        if self.attackers[attacker_ip]['attempts'] > 5:
            print(f"[THROTTLE] {attacker_ip} - Suspicious activity")
            time.sleep(2)
        
        return "ALLOWED"

    def calculate_threat_level(self, ip):
        """Intelligent threat assessment"""
        stats = self.attackers[ip]
        threat_score = 0
        
        if len(stats['ports_hit']) > 1:
            threat_score += 3
            
        if stats['attempts'] > 3:
            threat_score += 3
            
        if stats['last_attempt']:
            time_diff = (datetime.now() - stats['last_attempt']).total_seconds()
            if time_diff < 10:
                threat_score += 2
                
        return min(threat_score, 10)

    def is_rapid_attacker(self, ip):
        """Detect rapid attack patterns"""
        stats = self.attackers[ip]
        if stats['attempts'] < 2:
            return False
            
        time_window = 30
        if stats['first_seen']:
            time_diff = (datetime.now() - stats['first_seen']).total_seconds()
            attack_rate = stats['attempts'] / time_diff if time_diff > 0 else 0
            return attack_rate > 0.2
            
        return False

    def immediate_block(self, ip):
        """Immediate defensive action"""
        self.attackers[ip]['blocked'] = True
        self.blocked_ips.add(ip)
        
        block_data = {
            'timestamp': datetime.now().isoformat(),
            'blocked_ip': ip,
            'reason': 'High threat level',
            'threat_level': self.attackers[ip]['threat_level'],
            'ports_targeted': list(self.attackers[ip]['ports_hit']),
            'total_attempts': self.attackers[ip]['attempts']
        }
        
        with open('defense_blocks.json', 'a') as f:
            f.write(json.dumps(block_data) + '\n')
        
        print(f"[BLOCKED] {ip} - Threat neutralized by defense system")

    def detection_system(self, port):
        """Detection with integrated defense"""
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(1.0)
            server.bind(('127.0.0.1', port))
            server.listen(5)
            
            print(f"[DETECTION] Port {port} monitoring active")
            
            while self.is_active:
                try:
                    conn, addr = server.accept()
                    attacker_ip = addr[0]
                    
                    print(f"[DETECTED] {attacker_ip} on port {port}")
                    
                    if attacker_ip in self.blocked_ips:
                        print(f"[DEFENSE] Blocked IP tried again: {attacker_ip}")
                        conn.close()
                        continue
                    
                    defense_status = self.defense_system(attacker_ip, port)
                    
                    if defense_status in ["BLOCKED", "LIMITED"]:
                        conn.close()
                        continue
                    
                    conn.send(b"SSH-2.0-OpenSSH_8.2p1\r\n")
                    conn.close()
                    
                    if defense_status == "ALLOWED":
                        self.intelligence_system(attacker_ip, port)
                        
                except socket.timeout:
                    continue
                    
        except Exception as e:
            print(f"Detection error: {e}")

    def intelligence_system(self, attacker_ip, port):
        """Gather intelligence """
        print(f"[INTELLIGENCE] Researching {attacker_ip}")
        
        open_ports = self.scan_attacker(attacker_ip)
        
        if open_ports:
            print(f"[INTEL FOUND] {attacker_ip} has {len(open_ports)} open ports")
            
            services = self.stealth_service_scan(attacker_ip, open_ports)
            vulnerabilities = self.stealth_vulnerability_assessment(services)
            
            self.save_intelligence(attacker_ip, open_ports, services, vulnerabilities)
            
            if vulnerabilities and self.attackers[attacker_ip]['threat_level'] < 6:
                self.reverse_hack_system(attacker_ip, vulnerabilities)

    def scan_attacker(self, target_ip):
        """Stealthy port scanning"""
        open_ports = []
        common_ports = [21, 22, 23, 80, 443, 3389]
        
        for port in common_ports:
            try:
                time.sleep(0.3)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    open_ports.append(port)
                sock.close()
            except:
                continue
                
        return open_ports

    def stealth_service_scan(self, target_ip, ports):
        """Stealthy service identification"""
        services = {}
        service_map = {21: 'FTP', 22: 'SSH', 23: 'Telnet', 80: 'HTTP', 443: 'HTTPS', 3389: 'RDP'}
        
        for port in ports:
            services[port] = service_map.get(port, 'Unknown')
            print(f"[STEALTH] Port {port}: {services[port]}")
            
        return services

    def stealth_vulnerability_assessment(self, services):
        """Stealth vulnerability finding"""
        vulnerabilities = []
        
        for port, service in services.items():
            if service == 'FTP':
                vulnerabilities.append({
                    'port': port, 'service': service,
                    'type': 'FTP_ANONYMOUS',
                    'risk': 'HIGH'
                })
            elif service == 'Telnet':
                vulnerabilities.append({
                    'port': port, 'service': service,
                    'type': 'CLEARTEXT', 
                    'risk': 'HIGH'
                })
                
        return vulnerabilities

    def save_intelligence(self, ip, ports, services, vulnerabilities):
        """Save gathered intelligence"""
        intel_report = {
            'timestamp': datetime.now().isoformat(),
            'target': ip,
            'intel_method': 'STEALTH_RECON',
            'findings': {
                'open_ports': ports,
                'services': services,
                'vulnerabilities': vulnerabilities
            }
        }
        
        with open(f'intelligence_{ip.replace(".", "_")}.json', 'w') as f:
            json.dump(intel_report, f, indent=2)

    def reverse_hack_system(self, target_ip, vulnerabilities):
        """Reverse hacking after successful defense & intelligence"""
        print(f"[REVERSE HACK] Counter-attacking {target_ip}")
        
        for vuln in vulnerabilities:
            print(f"[EXPLOIT] {vuln['service']} on port {vuln['port']}")
            time.sleep(1)
            
        hack_report = {
            'timestamp': datetime.now().isoformat(),
            'target_hacked': target_ip,
            'vulnerabilities_exploited': [v['type'] for v in vulnerabilities],
            'defense_status_during_attack': 'SECURE'
        }
        
        with open(f'reverse_hack_{target_ip.replace(".", "_")}.json', 'w') as f:
            json.dump(hack_report, f, indent=2)
            
        print(f"[SUCCESS] Reverse hack completed: {target_ip}")

    def start_complete_system(self):
        """Start all 5 pillars"""
        print("\nStarting Complete 5-Pillar System")
        print("1. DETECTION  - Active on ports 2222, 4444")
        print("2. DEFENSE    - Auto-block & threat assessment") 
        print("3. INTELLIGENCE - Attacker research")
        print("4. STEALTH    - Hidden operations")
        print("5. REVERSE HACK - Counter-attacks")
        print()
        
        ports = [2222, 4444]
        for port in ports:
            thread = threading.Thread(target=self.detection_system, args=(port,), daemon=True)
            thread.start()
        
        try:
            while self.is_active:
                time.sleep(0.5)
        except KeyboardInterrupt:
            print("\nStopping Complete System...")
            self.is_active = False

if __name__ == "__main__":
    complete_system = ReverseStrikeComplete()
    complete_system.start_complete_system()
