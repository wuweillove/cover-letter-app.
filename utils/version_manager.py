import streamlit as st
from datetime import datetime
from typing import Dict, List, Optional
import json

class VersionManager:
    """Manage multiple versions of cover letters with history."""
    
    def __init__(self):
        if 'letter_versions' not in st.session_state:
            st.session_state.letter_versions = []
        if 'version_counter' not in st.session_state:
            st.session_state.version_counter = 0
    
    def save_version(self, content: str, metadata: Optional[Dict] = None) -> int:
        """Save a new version of the letter."""
        st.session_state.version_counter += 1
        
        version = {
            'id': st.session_state.version_counter,
            'content': content,
            'metadata': metadata or {},
            'timestamp': datetime.now().isoformat(),
            'word_count': len(content.split()),
            'char_count': len(content)
        }
        
        st.session_state.letter_versions.append(version)
        return version['id']
    
    def get_version(self, version_id: int) -> Optional[Dict]:
        """Get a specific version by ID."""
        for version in st.session_state.letter_versions:
            if version['id'] == version_id:
                return version
        return None
    
    def get_all_versions(self) -> List[Dict]:
        """Get all saved versions."""
        return st.session_state.letter_versions
    
    def get_latest_version(self) -> Optional[Dict]:
        """Get the most recent version."""
        if st.session_state.letter_versions:
            return st.session_state.letter_versions[-1]
        return None
    
    def delete_version(self, version_id: int) -> bool:
        """Delete a specific version."""
        for i, version in enumerate(st.session_state.letter_versions):
            if version['id'] == version_id:
                st.session_state.letter_versions.pop(i)
                return True
        return False
    
    def update_version(self, version_id: int, content: str, metadata: Optional[Dict] = None) -> bool:
        """Update an existing version."""
        for version in st.session_state.letter_versions:
            if version['id'] == version_id:
                version['content'] = content
                if metadata:
                    version['metadata'].update(metadata)
                version['modified_at'] = datetime.now().isoformat()
                version['word_count'] = len(content.split())
                version['char_count'] = len(content)
                return True
        return False
    
    def clear_all(self) -> bool:
        """Clear all versions."""
        st.session_state.letter_versions = []
        st.session_state.version_counter = 0
        return True
    
    def search_versions(self, query: str) -> List[Dict]:
        """Search versions by content or metadata."""
        query_lower = query.lower()
        results = []
        
        for version in st.session_state.letter_versions:
            # Search in content
            if query_lower in version['content'].lower():
                results.append(version)
                continue
            
            # Search in metadata
            metadata_str = json.dumps(version.get('metadata', {})).lower()
            if query_lower in metadata_str:
                results.append(version)
        
        return results
    
    def filter_by_metadata(self, key: str, value: str) -> List[Dict]:
        """Filter versions by metadata field."""
        return [
            version for version in st.session_state.letter_versions
            if version.get('metadata', {}).get(key) == value
        ]
    
    def get_statistics(self) -> Dict:
        """Get statistics about saved versions."""
        if not st.session_state.letter_versions:
            return {
                'total_versions': 0,
                'total_words': 0,
                'avg_words': 0,
                'oldest_date': None,
                'newest_date': None
            }
        
        word_counts = [v['word_count'] for v in st.session_state.letter_versions]
        timestamps = [v['timestamp'] for v in st.session_state.letter_versions]
        
        return {
            'total_versions': len(st.session_state.letter_versions),
            'total_words': sum(word_counts),
            'avg_words': int(sum(word_counts) / len(word_counts)),
            'min_words': min(word_counts),
            'max_words': max(word_counts),
            'oldest_date': min(timestamps),
            'newest_date': max(timestamps)
        }
    
    def export_all_versions(self) -> str:
        """Export all versions as JSON."""
        return json.dumps(st.session_state.letter_versions, indent=2)
    
    def import_versions(self, json_data: str) -> bool:
        """Import versions from JSON."""
        try:
            versions = json.loads(json_data)
            st.session_state.letter_versions.extend(versions)
            # Update counter
            if versions:
                max_id = max(v.get('id', 0) for v in versions)
                st.session_state.version_counter = max(st.session_state.version_counter, max_id)
            return True
        except Exception:
            return False
    
    def compare_versions(self, version_id1: int, version_id2: int) -> Dict:
        """Compare two versions and highlight differences."""
        v1 = self.get_version(version_id1)
        v2 = self.get_version(version_id2)
        
        if not v1 or not v2:
            return {}
        
        return {
            'version_1': {
                'id': v1['id'],
                'word_count': v1['word_count'],
                'timestamp': v1['timestamp'],
                'content': v1['content']
            },
            'version_2': {
                'id': v2['id'],
                'word_count': v2['word_count'],
                'timestamp': v2['timestamp'],
                'content': v2['content']
            },
            'differences': {
                'word_count_diff': v2['word_count'] - v1['word_count'],
                'char_count_diff': v2['char_count'] - v1['char_count']
            }
        }
